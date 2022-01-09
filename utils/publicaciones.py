import requests


def catalogoPublicaciones():
    url = "https://api.cammesa.com/pub-svc/public/catalogoPublicaciones"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGas():
    url = "https://api.cammesa.com/pub-svc/public/catalogoPublicacionesVigentes"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def findAllAttachmentZipByNemoId(doc_id, nemo):
    url = f"https://api.cammesa.com/pub-svc/public/findAllAttachmentZipByNemoId?docId={doc_id}&nemo={nemo}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGasPD(attachment_id, doc_id, nemo):
    url = f"https://api.cammesa.com/pub-svc/public/findAttachmentByNemoId?attachmentId={attachment_id}&docId={doc_id}&nemo={nemo}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def consumoGasPDPlanGas(desde, hasta, nemo):
    url = f"https://api.cammesa.com/pub-svc/public/findDocumentosByNemoRango?fechadesde={desde}&fechahasta={hasta}&nemo={nemo}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response


def costoMarginal(nemo):
    url = f"https://api.cammesa.com/pub-svc/public/obtieneFechaUltimoDocumento?nemo={nemo}"
    response = requests.request("GET", url)
    if response.status_code == 200:
        return response
