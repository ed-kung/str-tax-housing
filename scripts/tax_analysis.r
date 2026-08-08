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
INPUT_FILEPATH <- paste0(MY_DATA_PATH, "/processed_data/tax_analysis_panel.parquet")


# ---- Helper funcs

# Prettier theme
my_theme <- 
  theme(axis.text   = element_text(size=12, family="serif", face="plain", color="black"), 
        axis.title  = element_text(size=12, family="serif", face="plain", color="black"), 
        plot.title  = element_text(size=14, family="serif", face="plain", color="black"), 
        legend.text = element_text(size=12, family="serif", face="plain", color="black"))

# Returns CS DID estimator object
csdid <- function(dataframe, yname, gname) {
  o <- att_gt(
    yname = yname,
    gname = gname,
    tname = "year",
    idname = "id",
    data = dataframe,
    allow_unbalanced_panel = FALSE,
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

df <- read_parquet(INPUT_FILEPATH)

#df <- filter(df, year<2020)  # remove covid years
#df <- filter(df, year>=2019)  # use Davide time period


vars <- c(
  rev_general = "FiSC Revenue (All Sources)",
  rev_general_city = "City Revenue (All Sources)",
  taxes = "FiSC Tax Revenue (All Tax Sources)",
  taxes_city = "City Tax Revenue (All Tax Sources)",
  tax_property = "FiSC Property Tax Revenue",
  tax_property_city = "City Property Tax Revenue",
  tax_sales_general = "FiSC General Sales Tax Revenue",
  tax_sales_general_city = "City General Sales Tax Revenue",
  tax_income = "FiSC Income Tax Revenue",
  tax_income_city = "City Income Tax Revenue",
  tax_sales_selectiv = "FiSC Selective Sales Tax Revenue",
  tax_sales_selectiv_city = "City Selective Sales Tax Revenue",
  tax_licenses = "FiSC License Tax Revenue",
  tax_licenses_city = "City License Tax Revenue",
  tax_transfer = "FiSC Transfer Tax Revenue",
  tax_transfer_city = "City Transfer Tax Revenue",
  charges = "FiSC Charge Revenue",
  charges_city = "City Charge Revenue",
  rev_utility = "FiSC Utility Revenue",
  rev_utility_city = "City Utility Revenue",
  ZHVI = "City ZHVI"
)


results <- data.frame()

for (covid in c(TRUE, FALSE)) {

  my_results <- data.frame(
    outcome = unname(unlist(vars)),
    att = NA_real_,
    se = NA_real_,
    p = NA_real_
  )
  
  if (covid) {
    filename_append <- ""
    title_append <- ""
  } else {
    filename_append <- "_nocovid"
    title_append <- ", Year<2020"
  }
  
  for (i in seq_along(vars)) {
    col <- names(vars)[i]
    label <- vars[[i]]
    
    if (col %in% c("ZHVI", "A89")) {
      df$outcome <- log1p(df[[col]]*1000)
    } else {
      df$outcome <- log1p(df[[col]])
    }
    
    if (covid) {
      o <- csdid(df, "outcome", "effective_year")
    } else {
      o <- csdid(filter(df, year<2020), "outcome", "effective_year")
    }

    r <- aggte(o, type="simple", na.rm=TRUE)
    my_results$att[i] <- r$overall.att
    my_results$se[i] <- r$overall.se
    my_results$p[i] <- 2*pnorm(-abs(r$overall.att / r$overall.se))
    
    g <- es_graph(o, paste0(label, title_append), 6)
    print(g)
    filename <- paste0(ROOT_PATH, "/results/csdid_", col, filename_append, ".png")
    print(filename)
    ggsave(filename, plot = g, width=6, height=4)
  }
  my_results$covid <- covid
  results <- rbind(results, my_results)
}

results %>% 
  filter(p < 0.1) %>%
  print()
