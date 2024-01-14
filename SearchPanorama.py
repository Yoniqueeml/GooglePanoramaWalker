import json
import re

import requests as requests


def make_search_url(lat: float, lon: float):
    url = (
        "https://maps.googleapis.com/maps/api/js/"
        "GeoPhotoService.SingleImageSearch"
        "?pb=!1m5!1sapiv3!5sUS!11m2!1m1!1b0!2m4!1m2!3d{0:}!4d{1:}!2d50!3m10"
        "!2m2!1sen!2sGB!9m1!1e2!11m4!1m3!1e2!2b1!3e2!4m10!1e1!1e2!1e3!1e4"
        "!1e8!1e6!5m1!1e2!6m1!1e2"
        "&callback=callbackfunc"
    )
    return url.format(lat, lon)


def search_request(lat: float, lon: float):
    url = make_search_url(lat, lon)
    return requests.get(url)


def get_panoramas_id(text: str):
    blob = re.findall(r"callbackfunc\( (.*) \)$", text)[0]
    data = json.loads(blob)

    if data == [[5, "generic", "Search returned no images."]]:
        return []

    subset = data[1][5][0]

    raw_panos = subset[3][0]

    if len(subset) < 9 or subset[8] is None:
        raw_dates = []
    #else:
        #raw_dates = subset[8]

    raw_panos = raw_panos[::-1]
    #raw_dates = raw_dates[::-1]

    return raw_panos[0][1]


def search_panoramas(lat: float, lon: float):
    resp = search_request(lat, lon)
    pans = get_panoramas_id(resp.text)
    return pans
