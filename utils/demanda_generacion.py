import requests


def Agentes():
    url = "https://api.cammesa.com/demanda-svc/demanda/Agentes"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def CantDiasHabiles(desde, hasta):
    url = f"https://api.cammesa.com/demanda-svc/demanda/CantDiasHabiles?desde={desde}&hasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def EstacionesTransformadoras():
    url = "https://api.cammesa.com/demanda-svc/demanda/EstacionesTransformadoras"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def IntercambioCorredoresGeo():
    url = "https://api.cammesa.com/demanda-svc/demanda/IntercambioCorredoresGeo"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGasPDPlanGas(region):
    url = f"https://api.cammesa.com/demanda-svc/demanda/ObtieneDemandaYTemperaturaRegion?id_region={region}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def RegionesDemanda():
    url = "https://api.cammesa.com/demanda-svc/demanda/RegionesDemanda"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def TensionesNominales():
    url = "https://api.cammesa.com/demanda-svc/demanda/TensionesNominales"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def ObtieneGeneracioEnergiaPorRegion(region):
    url = f"https://api.cammesa.com/demanda-svc/generacion/ObtieneGeneracioEnergiaPorRegion?id_region={region}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response
