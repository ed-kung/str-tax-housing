"""
Tools for working with the Annual Survey of State and Local Government Finances (ALFIN) data

NOTES:
- ALFIN data is organized very differently for years <2012 compared to years >=2012
- Main variables to extract:
    - T19: Other Selective Sales Tax (hotel and occupancy taxes usually go here)
    - T28: Occupational and Business License Tax, NEC (str license fees maybe go here)
    - T29: Other License Tax (str license fees maybe go here)
    - U30: Fines and Forfeits (str fines maybe go here)
    - A03: Misc Commercial Activities NEC Charges (str charges maybe go here)
    - A89: All other NEC charges (str charges maybe go here)
"""

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

ALFIN_PATH = os.path.join(RAW_DATA_PATH, "alfin")

ITEM_COLMAP_2012_2016 = {
    "ID": (1, 14), 
    #"STATE_ID": (1, 2),  # state identifier is not FIPS for 2012-2016 so don't include
    "UNIT_TYPE_CODE": (3, 3),
    #"COUNTY_ID": (4, 6),  # county identifier is not FIPS for 2012-2016 so don't include
    "UNIT_ID": (7, 9),
    "PART_FLAG": (10, 14),  # should be 00000 to indicate unit is not part of another gov't unit
    "ITEM_CODE": (15, 17),
    "AMOUNT": (18, 29),  # amount is in thousands
    "YEAR": (30, 33),
    "IMPUTATION_FLAG": (34, 34)
}

UNIT_COLMAP_2012_2016 = {
    "ID": (1, 14),
    "UNIT_TYPE_CODE": (3,3),
    "NAME": (15, 78),
    "COUNTY_NAME": (79, 113),
    "STATE_FIPS": (114, 115),
    "COUNTY_FIPS": (116, 118),
    "PLACE_FIPS": (119, 123),
    "POPULATION": (124, 132),
    "POPULATION_YEAR": (133, 134),
    "ENROLLMENT": (135, 141),
    "ENROLLMENT_YEAR": (142, 143),
    "FUNCTION_CODE": (144, 145),
    "SCHOOL_LEVEL_CODE": (146, 147),
    "FISCAL_YEAR_ENDING": (148, 151),
    "SURVEY_YEAR": (152, 153)
}

ITEM_COLMAP_2017_2023 = {
    "ID": (1, 12),
    #"STATE_FIPS": (1, 2),  # don't include / will be included in the geo file
    "UNIT_TYPE_CODE": (3, 3),
    #"COUNTY_FIPS": (4, 6),  # don't include / will be included in the geo file
    "UNIT_ID": (7, 12),
    "ITEM_CODE": (13, 15),
    "AMOUNT": (16, 27),  # amount is in thousands
    "YEAR": (28, 31), 
    "IMPUTATION_FLAG": (32, 32)
}

UNIT_COLMAP_2017_2023 = {
    "ID": (1, 12),
    "UNIT_TYPE_CODE": (3,3),
    "NAME": (13, 76),
    "COUNTY_NAME": (77, 111),
    "STATE_FIPS": (1, 2),  # use positions 1-2 of ID
    "COUNTY_FIPS": (4, 6),  # use positions 4-6 of ID
    "PLACE_FIPS": (112, 116),
    "POPULATION": (117, 125),
    "POPULATION_YEAR": (126, 127),
    "ENROLLMENT": (128, 134),
    "ENROLLMENT_YEAR": (135, 136),
    "FUNCTION_CODE": (137, 138),
    "SCHOOL_LEVEL_CODE": (139, 140),
    "FISCAL_YEAR_ENDING": (141, 144),
    "SURVEY_YEAR": (145, 146)
}

ALFIN_FILES = {
    "2007": {
        "filename": "historical_1967_2012/IndFin07a.Txt"
    },
    "2008": {
        "filename": "historical_1967_2012/IndFin08a.Txt"
    },
    "2009": {
        "filename": "historical_1967_2012/IndFin09a.Txt"
    },
    "2010": {
        "filename": "historical_1967_2012/IndFin10a.Txt"
    },
    "2011": {
        "filename": "historical_1967_2012/IndFin11a.Txt"
    },
    "2012": {
        "item_filename": "2012/2012FinEstDAT_10162019modp_pu.txt",
        "unit_filename": "2012/Fin_GID_2012.txt",
        "item_columns": ITEM_COLMAP_2012_2016,
        "unit_columns": UNIT_COLMAP_2012_2016
    },
    "2013": {
        "item_filename": "2013/2013FinEstDAT_10162019modp_pu.txt",
        "unit_filename": "2013/Fin_GID_2013.txt",
        "item_columns": ITEM_COLMAP_2012_2016,
        "unit_columns": UNIT_COLMAP_2012_2016
    },
    "2014": {
        "item_filename": "2014/2014FinEstDAT_10162019modp_pu.txt",
        "unit_filename": "2014/Fin_GID_2014.txt",
        "item_columns": ITEM_COLMAP_2012_2016,
        "unit_columns": UNIT_COLMAP_2012_2016
    },
    "2015": {
        "item_filename": "2015/2015FinEstDAT_10162019modp_pu.txt",
        "unit_filename": "2015/Fin_GID_2015.txt",
        "item_columns": ITEM_COLMAP_2012_2016,
        "unit_columns": UNIT_COLMAP_2012_2016
    },
    "2016": {
        "item_filename": "2016/2016FinEstDAT_10162019modp_pu.txt",
        "unit_filename": "2016/Fin_GID_2016.txt",
        "item_columns": ITEM_COLMAP_2012_2016,
        "unit_columns": UNIT_COLMAP_2012_2016
    },
    "2017": {
        "item_filename": "2017/2017FinEstDAT_09202024modp_pu.txt",
        "unit_filename": "2017/Fin_PID_2017.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    },
    "2018": {
        "item_filename": "2018/2018FinEstDAT_09202024modp_pu.txt",
        "unit_filename": "2018/Fin_PID_2018.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    },
    "2019": {
        "item_filename": "2019/2019FinEstDAT_09202024modp_pu.txt",
        "unit_filename": "2019/Fin_PID_2019.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    },
    "2020": {
        "item_filename": "2020/2020FinEstDAT_09202024modp_pu.txt",
        "unit_filename": "2020/Fin_PID_2020.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    },
    "2021": {
        "item_filename": "2021/2021FinEstDAT_09202024modp_pu.txt",
        "unit_filename": "2021/Fin_PID_2021.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    },
    "2022": {
        "item_filename": "2022/2022_Individual_Unit_File/2022FinEstDAT_06052025modp_pu.txt",
        "unit_filename": "2022/2022_Individual_Unit_File/Fin_PID_2022.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    },
    "2023": {
        "item_filename": "2023/2023_Individual_Unit_Files/2023FinEstDAT_06052025modp_pu.txt",
        "unit_filename": "2023/2023_Individual_Unit_Files/Fin_PID_2023.txt",
        "item_columns": ITEM_COLMAP_2017_2023,
        "unit_columns": UNIT_COLMAP_2017_2023
    }
} 



# Helper function for reading in item level data
def _get_item_data(year):
    year_s = str(year)
    year_i = int(year)
    if year >= 2012:
        filepath = os.path.join(ALFIN_PATH, ALFIN_FILES[year_s]["item_filename"])
        columns = ALFIN_FILES[year_s]["item_columns"]
        df = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                row = {}
                for k, v in columns.items():
                    start = v[0]-1
                    end = v[1]
                    row[k] = line[start:end].strip()
                df.append(row)
        df = pd.DataFrame(df)
        df['AMOUNT'] = df['AMOUNT'].astype(float)
        df['YEAR'] = df['YEAR'].astype(int)
        return df
    else:
        filepath = os.path.join(ALFIN_PATH, ALFIN_FILES[year_s]["filename"])
        return pd.read_csv(filepath)

# Helper function for reading in unit level data
def _get_unit_data(year):
    year_s = str(year)
    year_i = int(year)
    if year >= 2012:
        filepath = os.path.join(ALFIN_PATH, ALFIN_FILES[year_s]["unit_filename"])
        columns = ALFIN_FILES[year_s]["unit_columns"]
        df = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                row = {}
                for k, v in columns.items():
                    start = v[0]-1
                    end = v[1]
                    row[k] = line[start:end].strip()
                df.append(row)
        df = pd.DataFrame(df)
        return df
    else:
        filepath = os.path.join(ALFIN_PATH, ALFIN_FILES[year_s]["filename"])
        return pd.read_csv(filepath)

