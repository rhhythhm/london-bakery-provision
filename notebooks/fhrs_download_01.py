import pandas as pd
import requests

#Downloading data from api
BASE_URL = "https://api.ratings.food.gov.uk"

HEADERS = {
    "x-api-version": "2",
    "Accept": "application/json",
}

response = requests.get(
    f"{BASE_URL}/Authorities",
    headers=HEADERS,
    timeout=30,
)

response.raise_for_status()

#Api response structure
authority_payload = response.json()

print(authority_payload.keys())
authority_payload.get("meta", {})

authorities = pd.DataFrame(authority_payload["authorities"])

#Basic exploratory analysis on dataset
print(authorities.shape)
print(authorities.columns.tolist())

authorities.head()


#Inspecting datatypes
authorities.info()

authorities.dtypes

#Inspecting sparsity of data
authority_missingness = pd.DataFrame({
    "missing_count": authorities.isna().sum(),
    "missing_percentage": (authorities.isna().mean() * 100).round(2),
    }
    ).sort_values("missing_percentage", ascending=False,)

print(authority_missingness)

#Checking the number of london authorities that are found in the data
london_authorities = authorities[
    authorities["RegionName"]
    .astype(str)
    .str.strip()
    .str.casefold()
    .eq("london")].copy()

print(f"Number of London authorities found: {len(london_authorities)}")

london_authorities[
    ["LocalAuthorityId", "Name", "EstablishmentCount", "LastPublishedDate",]
    ].sort_values("Name")