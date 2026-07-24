library(here)
library(did)
library(fixest)
library(dplyr)
library(yaml)
library(arrow)
library(ggplot2)

readRenviron(here(".env"))

ROOT_PATH <- Sys.getenv("ROOT_PATH")
MY_DATA_PATH <- Sys.getenv("MY_DATA_PATH")

# ---- Helper funcs

# Prettier theme
my_theme <- 
  theme(axis.text   = element_text(size=12, family="serif", face="plain", color="black"), 
        axis.title  = element_text(size=12, family="serif", face="plain", color="black"), 
        plot.title  = element_text(size=14, family="serif", face="plain", color="black"), 
        legend.text = element_text(size=12, family="serif", face="plain", color="black"))

# Returns CS DID estimator object
csdid <- function(yname, gname) {
  o <- att_gt(
    yname = yname,
    gname = gname,
    tname = "year",
    idname = "city_id",
    data = df,
    allow_unbalanced_panel = TRUE,
    control_group = "notyettreated"
  )
  return(o)
}

# Creates event study plot
es_graph <- function(att_gt_object, title, bw, bal=NULL) {
  es <- aggte(att_gt_object, type="dynamic", min_e=-bw, max_e=bw, balance_e=bal, na.rm=TRUE, bstrap=FALSE)
  g <- ggdid(es) + 
    ggtitle(title) + 
    xlab("Years Since Regulation") + 
    ylab(NULL) + 
    xlim(-bw,bw) + 
    scale_x_continuous(breaks=seq(-bw,bw)) + 
    my_theme 
  return(g)
}


# ---- Data analysis

INPUT_FILEPATH <- paste0(MY_DATA_PATH, "/tax_analysis_panel.parquet")

df <- read_parquet(INPUT_FILEPATH)

#df <- filter(df, abs(years_from_enforcement)<=12)  # +/- 12 years from enforcement

vars <- c(
  rev_general_city = "City Revenue (All Sources)",
  taxes_city = "City Tax Revenue (All Tax Sources)",
  tax_property_city = "City Property Tax Revenue",
  tax_sales_general_city = "City General Sales Tax Revenue",
  tax_income_city = "City Income Tax Revenue",
  tax_license_bus_city = "City Business and Occupation License Tax Revenue",
  tax_sales_other_city = "City Selective Sales Tax Revenue",
  charges = "City Revenue from Charge Fees",
  ZHVI = "City ZHVI"
)

for (col in names(vars)) {
  label <- vars[[col]]
  df$outcome <- log1p(df[[col]])
  o <- csdid("outcome", "enforcement_year")
  g <- es_graph(o, label, 6)
  print(g)
  filename <- paste0(ROOT_PATH, "/results/csdid_", col, ".png")
  print(filename)
  ggsave(filename, plot = g, width=6, height=4)
}

