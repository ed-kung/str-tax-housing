library(did)
library(fixest)
library(dplyr)
library(yaml)
library(arrow)
library(ggplot2)

LOCAL_CONFIG <- read_yaml("../../config.local.yaml")
LOCAL_PATH <- LOCAL_CONFIG["LOCAL_PATH"][[1]]
DATA_PATH <- LOCAL_CONFIG["DATA_PATH"][[1]]

# ---- Helper funcs

my_theme <- 
  theme(axis.text   = element_text(size=12, family="serif", face="plain", color="black"), 
        axis.title  = element_text(size=12, family="serif", face="plain", color="black"), 
        plot.title  = element_text(size=14, family="serif", face="plain", color="black"), 
        legend.text = element_text(size=12, family="serif", face="plain", color="black"))

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

es_graph <- function(att_gt_object, title, bw, bal=NULL) {
  es <- aggte(att_gt_object, type="dynamic", min_e=-bw, max_e=bw, balance_e=bal, na.rm=TRUE, bstrap=FALSE)
  g <- ggdid(es) + 
    ggtitle(title) + 
    xlab("Years Since Regulation") + 
    ylab(NULL) + 
    xlim(-bw,bw) + 
    scale_x_continuous(breaks=seq(-bw,bw,12)) + 
    my_theme 
  return(g)
}

# ---- Data analysis

in_filename <- paste0(DATA_PATH, "/tax_analysis_panel.parquet")

df <- read_parquet(in_filename)

vars <- c(
  rev_general = "City Revenue (All Sources)",
  taxes = "City Tax Revenue (All Tax Sources)",
  tax_property = "City Property Tax Revenue",
  tax_sales_general = "City Sales Tax Revenue",
  tax_income = "City Income Tax Revenue",
  tax_licenses = "City Licensing Tax Revenue",
  charges = "City Revenue from Charge Fees"
)

for (col in names(vars)) {
  label <- vars[[col]]
  df$outcome <- log1p(df[[col]])
  o <- csdid("outcome", "enforcement_year")
  g <- es_graph(o, label, 12)
  print(g)
  filename <- paste0(LOCAL_PATH, "/results/csdid_", col, ".png")
  print(filename)
  ggsave(filename, plot = g, width=6, height=4)
}

