import requests
from requests import Response

URL_BASE = "https://download.beta.ons.gov.uk/downloads/datasets/regional-gdp-by-quarter/editions/time-series/versions/4.csv"


def get_data_frame(
    start_period: str = "1900-01-01",
    end_period: str = None,
) -> str:
    request_url = URL_BASE

    try:
        abc: Response = requests.get(request_url)
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(
            f"HTTP error fetching data for {URL_BASE}:",
            abc.status_code,
            abc.reason,
            URL_BASE,
        ) from err
    return abc.text
