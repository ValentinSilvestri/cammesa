import requests


def caudalesSemanales(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/caudalesSemanales?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGas(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGas?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGasCD(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGasCD?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGasPD(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGasPD?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGasPDPlanGas(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGasPDPlanGas?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def costoMarginal(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/costoMarginal?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def cubrimientoPico(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/cubrimientoPico?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def cuencasDatosHidraulicos(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/cuencasDatosHidraulicos?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def ordenamientoRes240(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/ordenamientoRes240?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiEventoFalla(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiEventoFalla?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiEventoFallaNotifENRE(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiEventoFallaNotifENRE?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiFallaSisTrans(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiFallaSisTrans?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiFallaSisTrans500KV(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiFallaSisTrans500KV?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiFallaSuministroGen(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiFallaSuministroGen?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiNormalEventoFalla(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiNormalEventoFalla?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def perturbacionesSadiTodas(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiTodas?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def precioMercadoDef(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/precioMercadoDef?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def precioMercadoPD(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/precioMercadoPD?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def precioMercadoRedesp(desde, hasta):
    url = f"https://api.cammesa.com/pub-svc/public/especial/precioMercadoRedesp?fechadesde={desde}&fechahasta={hasta}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response
