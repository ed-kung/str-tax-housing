library(did)
library(fixest)
library(dplyr)
library(yaml)
library(arrow)

LOCAL_CONFIG <- read_yaml("../../config.local.yaml")
LOCAL_PATH <- LOCAL_CONFIG["LOCAL_PATH"][[1]]
DATA_PATH <- LOCAL_CONFIG["DATA_PATH"][[1]]

in_filename <- paste0(DATA_PATH, "/tax_analysis_panel.parquet")

df <- read_parquet(in_filename)

df$outcome <- log1p(df$tax_licenses)

csdid <- att_gt(
  yname = "outcome",
  gname = "enforcement_year",
  tname = "year",
  idname = "city_id",
  data = df,
  allow_unbalanced_panel = TRUE,
  control_group = "notyettreated"
)

aggte(csdid, type="simple", na.rm=TRUE, bstrap=TRUE)


