import requests


class PublicacionesEspeciales(object):

    def __init__(self):
        pass

    @staticmethod
    def caudalesSemanales(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/caudalesSemanales?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGas(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGas?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGasCD(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGasCD?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGasPD(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGasPD?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGasPDPlanGas(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/consumoGasPDPlanGas?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def costoMarginal(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/costoMarginal?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def cubrimientoPico(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/cubrimientoPico?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def cuencasDatosHidraulicos(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/cuencasDatosHidraulicos?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def ordenamientoRes240(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/ordenamientoRes240?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiEventoFalla(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiEventoFalla?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiEventoFallaNotifENRE(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiEventoFallaNotifENRE?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiFallaSisTrans(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiFallaSisTrans?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiFallaSisTrans500KV(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiFallaSisTrans500KV?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiFallaSuministroGen(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiFallaSuministroGen?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiNormalEventoFalla(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiNormalEventoFalla?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def perturbacionesSadiTodas(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/perturbacionesSadiTodas?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def precioMercadoDef(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/precioMercadoDef?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def precioMercadoPD(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/precioMercadoPD?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def precioMercadoRedesp(desde, hasta):
        url = f"https://api.cammesa.com/pub-svc/public/especial/precioMercadoRedesp?fechadesde={desde}&fechahasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response


class Publicaciones(object):

    def __init__(self):
        pass

    @staticmethod
    def catalogoPublicaciones():
        url = "https://api.cammesa.com/pub-svc/public/catalogoPublicaciones"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGas():
        url = "https://api.cammesa.com/pub-svc/public/catalogoPublicacionesVigentes"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def findAllAttachmentZipByNemoId(doc_id, nemo):
        url = f"https://api.cammesa.com/pub-svc/public/findAllAttachmentZipByNemoId?docId={doc_id}&nemo={nemo}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGasPD(attachment_id, doc_id, nemo):
        url = f"https://api.cammesa.com/pub-svc/public/findAttachmentByNemoId?attachmentId={attachment_id}&docId={doc_id}&nemo={nemo}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGasPDPlanGas(desde, hasta, nemo):
        url = f"https://api.cammesa.com/pub-svc/public/findDocumentosByNemoRango?fechadesde={desde}&fechahasta={hasta}&nemo={nemo}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def costoMarginal(nemo):
        url = f"https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo={nemo}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response


class DemandaGeneracion(object):

    def __init__(self):
        pass

    @staticmethod
    def Agentes():
        url = "https://api.cammesa.com/demanda-svc/demanda/Agentes"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def CantDiasHabiles(desde, hasta):
        url = f"https://api.cammesa.com/demanda-svc/demanda/CantDiasHabiles?desde={desde}&hasta={hasta}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def EstacionesTransformadoras():
        url = "https://api.cammesa.com/demanda-svc/demanda/EstacionesTransformadoras"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def IntercambioCorredoresGeo():
        url = "https://api.cammesa.com/demanda-svc/demanda/IntercambioCorredoresGeo"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def consumoGasPDPlanGas(region):
        url = f"https://api.cammesa.com/demanda-svc/demanda/ObtieneDemandaYTemperaturaRegion?id_region={region}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def RegionesDemanda():
        url = "https://api.cammesa.com/demanda-svc/demanda/RegionesDemanda"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def TensionesNominales():
        url = "https://api.cammesa.com/demanda-svc/demanda/TensionesNominales"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response

    @staticmethod
    def ObtieneGeneracioEnergiaPorRegion(region):
        url = f"https://api.cammesa.com/demanda-svc/generacion/ObtieneGeneracioEnergiaPorRegion?id_region={region}"
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response


