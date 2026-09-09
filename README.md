# Identifying Relative Under-Provision of Bakeries in London

MSc Data Science project analysing the spatial distribution and relative provision of bakery establishments across Greater London Middle Layer Super Output Areas (MSOAs).

The project constructs a bakery-establishment dataset from Food Hygiene Rating Scheme (FHRS) records, classifies establishments under three definitions of bakery provision, assigns them to London MSOAs to model expected bakery counts using MSOA-level population, transport and household-income.

Relative under-provision is interpreted as model-based shortfall within the study area and not as direct evidence of unmet consumer demand or commercial opportunity.

## Repository structure

```text
...
├── notebooks/              Jupyter notebooks containing the project workflow
│
├── data/                   Raw, intermediate and processed project datasets
│   ├── business/
│   │   ├── raw/
│   │   ├── interim/
│   │   └── processed/
│   │
│   └── spatial/
│       ├── raw/
│       └── processed/
│
├── models/                 Trained bakery-name classification models
│
├── outputs/
│   ├── figures/            Figures produced for analysis and the report
│   ├── tables/             Tabular report outputs
│   └── models/             Statistical model results and predictions
│
├── requirements.txt        Python package requirements
├── .gitignore              Files excluded from version control
└── README.md               Project overview and instructions
```

## Description of Notebooks

| Notebook                                   | Purpose                                                                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `01_fhrs_download.ipynb`                   | Downloads a dated Greater London FHRS establishment snapshot.                                                    |
| `02_fhrs_prepare_dataset.ipynb`            | Cleans and prepares FHRS establishment records.                                                                  |
| `03_osm_training_data_download.ipynb`      | Uses Overpass API to retrieve and prepare OpenStreetMap proxy-labelled training data.                            |
| `04_osm_initial_bakery_classifier.ipynb`   | Develops initial OSM bakery-name classifier and evaluates it.                                                    |
| `05_fhrs_classifier_application.ipynb`     | Applies the initial OSM-only classifier to FHRS business names and explores limitations.                         |
| `06_companies_house_data_download.ipynb`   | Uses Companies House advanced-search API to retrieve and prepare additional proxy-labelled training data.        |
| `07_final_bakery_classifier.ipynb`         | Evaluates final classifier configurations, selecting high-recall model and ranking FHRS bakery candidates.       |
| `08_bakery_ai_verification.ipynb`          | Performs search-grounded automated verification process on bakery-candidates using Gemini 2.5 Flash.             |
| `08b_supermarket_bakery_supplement.ipynb`  | Identifies and verifies supplementary supermarket bakery provision.                                              |
| `09_manual_review.ipynb`                   | Applies diagnostic rules to identify establishments for targeted manual review.                                  |
| `09b_multistore_establishment_check.ipynb` | Performs location-specific verification for business names represented by multiple FHRS establishments.          |
| `10_bakery_review_final_dataset.ipynb`     | Consolidates automated and manual decisions to create the final bakery dataset and performs validation.          |
| `11_london_msoa_spatial_process.ipynb`     | Prepares the 2021 Greater London MSOA boundary dataset.                                                          |
| `12_msoa_to_bakeries_lookup.ipynb`         | Assigns final bakery establishments to MSOAs, creating bakery counts under three definitions.                    |
| `13_ons_msoa_population.ipynb`             | Prepares ONS Mid-2024 MSOA population estimates for Greater London MSOAs.                                        |
| `14_naptan_transport_nodes.ipynb`          | Assigns and aggregates active NaPTAN transport stop points within respective London MSOAs.                       |
| `15_msoa_modelling_dataset.ipynb`          | Combines bakery counts and MSOA-level characteristics into final analysis and modelling dataset.                 |
| `16_msoa_bakery_analysis.ipynb`            | Performs exploratory and descriptive analysis of bakery provision.                                               |
| `17_msoa_bakery_count_model.ipynb`         | Fits and compares performance of Poisson and Negative Binomial bakery-count model.                               |
| `17b_msoa_bakery_count_model_income.ipynb` | Extends count models with MSOA-level average household incomes.                                                  |
| `18_msoa_bakery_underprovision.ipynb`      | Calculates standardised relative shortfall and produces under-provision rankings and maps.                       |
| `19_msoa_bakery_model_evaluation.ipynb`    | Evaluates ranking sensitivity against alternative bakery definitions and baseline measures.                      |


## Environment

The notebooks were developed using Python 3.14.5.

Create and activate a virtual environment, then install the required packages:

`python -m venv .venv`

Windows:

`.venv\Scripts\activate`

Install dependencies:

`pip install -r requirements.txt`

The main dependencies are listed in requirements.txt.


## Data sources

The project uses publicly available data from:

- Food Standards Agency Food Hygiene Rating Scheme (FHRS)
- OpenStreetMap
- Companies House
- Office for National Statistics 2021 MSOA boundaries
- Office for National Statistics postcode geography lookup
- Office for National Statistics Mid-2024 MSOA population estimates
- Department for Transport NaPTAN stop-point data
- Office for National Statistics small-area household-income estimates

Exact dataset versions and access dates are documented in the project report.

Large raw third-party datasets are not stored in the repository and should be obtained from their original sources.

## Running and inspecting the project

The notebooks are numbered in the approximate order of the project workflow and use paths relative to the `notebooks/` directory. They should therefore be opened and run from that directory, for example by using VS Code with the project virtual environment selected for the notebook kernel.

The repository includes the processed datasets and saved outputs required to inspect the completed analysis. Large raw third-party datasets are not included in version control, so a complete rerun from Notebook 01 requires the original source data and external API access for some stages.

### Recommended inspection

The saved outputs within the notebooks, `data/` and `outputs/` allow the completed project to be inspected without rerunning the data-acquisition or automated-verification stages.

The later analysis can be reproduced from the processed files included in the repository. Notebooks 15, 16 and 17 can be rerun directly from the included processed datasets. Notebook 17b additionally requires the original ONS household-income workbook.

The saved output from Notebook 17b is included in the repository, allowing Notebooks 18 and 19 to be rerun without repeating the income-model stage.

### Full rebuild

A complete rebuild follows the numbered notebook workflow from Notebook 01 onwards. This would require raw external datasets described and API credentials where indicated. Results obtained from external APIs or Google Search at a later date may differ from the dated project results.

## Raw data required for a complete rebuild

Large raw files were excluded from the repository. The following files are required to rerun the corresponding stages:

| Notebook | Required raw input |
|---|---|
| 10 | `data/business/raw/london_fhrs_raw_2026-07-23.csv` |
| 11 | 2021 MSOA shapefiles in `data/spatial/raw/msoa2021/` |
| 12 | `data/spatial/raw/msoa_lookup_data.csv` |
| 13 | `data/spatial/raw/ons_msoa_population_data.xlsx` |
| 14 | `data/spatial/raw/national_stop_data.csv` |
| 17b | `data/spatial/raw/ons_msoa_income_fye2023.xlsx` |

Notebooks 01, 03 and 06 acquire their source data programmatically, but dataset sources and versions are documented in the project report.

## API-dependent stages

The following notebooks require external API access:

- Notebook 01 uses the FHRS API.
- Notebook 03 uses the OpenStreetMap Overpass API.
- Notebook 06 uses the Companies House API and requires a Companies House API key.
- Notebooks 08, 08b and 09b use Gemini 2.5 Flash with Google Search grounding and require a Gemini API key.

API keys are not stored in the repository.

The automated verification stages were run using dated snapshots and the classification outputs used by subsequent stages are available in data folders so that expensive API verification does not need to be repeated when inspecting the completed analysis.

## Manual-review stages

The bakery-identification pipeline contains manual-review stages found in Notebooks 09 and 10.

Diagnostic rules in Notebook 09 were used to select potentially inconsistent classifications for targeted review. Manual-reviews can be found in `data/business/interim/ai_verification_v2/manual_review` and `data/business/interim/ai_verification_v3/manual_review_v3`

Notebook 10 combines these review decisions with automated results and contains the final class-stratified validation of bakery establishments.

## Bakery definitions

Three cumulative definitions of bakery provision are used:

- Core only: `CORE_BAKERY`
- Core and café: `CORE_BAKERY + BAKERY_CAFE`
- All provision included: `CORE_BAKERY + BAKERY_CAFE + GROCER_BAKERY`

The core-and-café definition is used for the primary under-provision analysis, with the other definitions retained for sensitivity analysis.

## Outputs

Project outputs are organised under the `outputs/` directory:

- `outputs/figures/` contains the figures and maps produced for the analysis and report.
- `outputs/tables/` contains tabular summaries that were featured in the report.
- `outputs/models/` contains statistical-model outputs, predictions and evaluation.

Processed datasets used by later stages of the pipeline are stored within the relevant `data/business/` and `data/spatial/` folders.

## Reproducibility notes

The analysis used open-source dated snapshots of datasets so that the results reported remain fixed to the study dataset. External APIs, source datasets and Google Search results can change over time, so a complete rerun at a later date is likely to not reproduce the original acquisition or the verification results.

Processed datasets, automated-verifiction datasets, completed manual-review decisions, and final analytical outputs are retained in the repository for completed analysis to be inspected without repeating these stages. Random sampling and model-validation stages use fixed random seeds where applicable to improve reproducibility. API keys and other credentials are, however, not stored in the repository.