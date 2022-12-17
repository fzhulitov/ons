import requests
import json


URL_BASE = "https://api.beta.ons.gov.uk/v1/datasets/"


def get_data_frame(key: str = "regional-gdp-by-quarter") :
    request_url = URL_BASE+key
    d = _connect_to_uk_api(request_url)
    url_ts = d['links']['latest_version']['href']
    csv_link = _connect_to_uk_api(url_ts)['downloads']['csv']['href']
    df = _connect_to_uk_api(csv_link, request_type='csv')
    return df


def _connect_to_uk_api(url: str, request_type: str = 'json') -> dict:
    session = requests.session()
    r = session.get(url=url)
    if r.status_code != requests.codes.ok:
        raise Exception(r.status_code, r.reason, url)
    session.close()
    if request_type == 'json':
        return json.loads(r.text)
    elif request_type == 'csv':
        return r.text
