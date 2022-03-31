import requests


class Jsons:
    NewYork = {
        "ip": "161.185.160.93",
        "city": "New York City",
        "region": "New York",
        "country": "US",
        "loc": "40.7143,-74.0060",
        "org": "AS22252 The City of New York",
        "postal": "10004",
        "timezone": "America/New_York",
        "readme": "https://ipinfo.io/missingauth"
    }

    Jerusalem = {
        "ip": "89.138.45.91",
        "hostname": "89-138-45-91.bb.netvision.net.il",
        "city": "Jerusalem",
        "region": "Jerusalem",
        "country": "IL",
        "loc": "31.7690,35.2163",
        "org": "AS1680 Cellcom Fixed Line Communication L.P.",
        "timezone": "Asia/Jerusalem",
        "readme": "https://ipinfo.io/missingauth"
    }

    Blairgowrie = {
        "ip": "86.138.45.91",
        "hostname": "host86-138-45-91.range86-138.btcentralplus.com",
        "city": "Blairgowrie",
        "region": "Scotland",
        "country": "GB",
        "loc": "56.5916,-3.3405",
        "org": "AS2856 British Telecommunications PLC",
        "postal": "PH10",
        "timezone": "Europe/London",
        "readme": "https://ipinfo.io/missingauth"
    }


def sendRequest(IP):
    r = requests.get(url=IP)
    return r.json()
