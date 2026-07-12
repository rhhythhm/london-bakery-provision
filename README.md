# london-bakery-provision
MSc Data Science project analysing relative bakery provision across London MSOAs using open data.

# Identifying Relative Under-Provision of Bakeries in London

This repository contains the implementation and documentation for the MSc Data Science project which aims to examine bakery provision across London's Middle Layer Super Output Areas (MSOAs).

## Project aim

The project aims to create a reproducible MSOA-level analysis that:

- Define rules to be used to reproducibly classify “bakery” establishments and use this to
create subset datasets of bakeries in London using open data.
- Collect and prepare datasets on London bakery, postcodes, respective MSOAs,
populations, and accessibility indicators.
- Construct an MSOA-level feature table, containing bakery counts, covariates, and a
derived measure of provision.
- Create an interpretable statistical model to estimate expected bakery counts in London
MSOAs and compare this with observed bakery counts.
- Identify and map relative under-provision and evaluate using baseline comparisons,
sensitivity checks.

The results will be interpreted as relative provision indicators rather than predictions of true demand, profitability or optimal business locations.

## Planned data sources

- Food Hygiene Rating Scheme food-business records
- ONS postcode-to-MSOA lookup data
- ONS MSOA population estimates
- ONS MSOA boundary data
- NaPTAN transport access points

## Planned tools

- Python
- pandas
- statsmodels
- matplotlib
- QGIS/GeoPandas
- GitHub

## Current status

Project design and repository setup.
