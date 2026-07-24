# %%
# Build main diff-in-diff analysis data

import os
import pandas as pd
import numpy as np
import dotenv

import warnings
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)

dotenv.load_dotenv(dotenv.find_dotenv())

ROOT_PATH = os.getenv("ROOT_PATH")
MY_DATA_PATH = os.getenv("MY_DATA_PATH")
RAW_DATA_PATH = os.getenv("RAW_DATA_PATH")

OUTPUT_FILEPATH = os.path.join(MY_DATA_PATH, "tax_analysis_panel.parquet")


# %%
# Load data

regs_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "sales-analysis-redfin/data/best_treatment_dates_2026-07.csv"))
tax_df = pd.read_excel(os.path.join(RAW_DATA_PATH, "lincoln-institute/FiSC-Full-Dataset-2023-Update.xlsx"), sheet_name="Data")
zhvi_df = pd.read_csv(os.path.join(RAW_DATA_PATH, "zhvi/City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"))
mapping = pd.read_csv(os.path.join(MY_DATA_PATH, "city_mapping.csv"))

# %%
# Reshape zhvi data long by year

id_cols = ['RegionID', 'SizeRank', 'RegionName', 'RegionType',
           'StateName', 'State', 'Metro', 'CountyName']

zhvi_long = zhvi_df.melt(
    id_vars=id_cols,
    var_name = 'date',
    value_name = 'ZHVI'
)

zhvi_long['date'] = pd.to_datetime(zhvi_long['date'])
zhvi_long['year'] = zhvi_long['date'].dt.year

zhvi_long = zhvi_long.groupby(id_cols + ['year']).agg({'ZHVI': 'mean'}).reset_index()


# %%
# Merging the data

df = regs_df.merge(
    mapping.rename(columns={'policy_city': 'city'}),
    on='city',
    how='left'
)

df = df.merge(
    tax_df.rename(columns={'city_name': 'tax_city'}),
    on='tax_city',
    how='left'
)

df = df.merge(
    zhvi_long,
    on=['RegionID', 'year'],
    how='inner'
)



# %%
# clean dates

df['best_enforcement'] = pd.to_datetime(df['best_enforcement'], errors='coerce')
df['best_passage'] = pd.to_datetime(df['best_passage'], errors='coerce')

df['enforcement_year'] = df['best_enforcement'].dt.year
df['passage_year'] = df['best_passage'].dt.year

df['years_from_enforcement'] = (df['year'] - df['enforcement_year'])
df['years_from_passage'] = (df['year'] - df['passage_year'])


# %%
# for cities with an enforcement date, drop rows >12 years to/from enforcement

mask = (np.abs(df['years_from_enforcement']) > 12) & (df['years_from_enforcement'].notna())
df = df.loc[~mask].reset_index(drop=True)

# for cities without an enforcement date, drop years outside the min/max of the remaining data

year_min = df.loc[df['best_enforcement'].notna(), 'year'].min()
year_max = df.loc[df['best_enforcement'].notna(), 'year'].max()
mask = (df['year'] < year_min) | (df['year'] > year_max)
df = df.loc[~mask].reset_index(drop=True)

# %%
# change enforcement and passage year to 0 for cities without enforcement/passage dates
# (standard convention for CSDID package in R)

df.loc[df['best_enforcement'].isna(), 'enforcement_year'] = 0
df.loc[df['best_passage'].isna(), 'passage_year'] = 0

df['enforcement_year'] = df['enforcement_year'].astype(int)
df['passage_year'] = df['passage_year'].astype(int)


# %%
# make a city_id integer (also required for CSDID package)

df['city_id'] = df['city'].astype('category').cat.codes

# %%
# output dataframe for analysis

df.to_parquet(OUTPUT_FILEPATH)
df.info()


