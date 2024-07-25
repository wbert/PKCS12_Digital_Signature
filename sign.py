import datetime
from endesive import pdf
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12


def main(
    x: float,
    x1: float,
    y: float,
    y1: float,
    pdfimage: str,
    p12signature: str,
    password: str,
    flname: str,
    page: int,
    reason="",
):
    """
    This function does the signature part
    PARAMETERS
    - x: float, horizontal position of the signature box
    - x1: float, width of the signature box
    - y: float, veritcal position of the signature box
    - y1: float, width of the signature box
    - pdfimage: str, path of the icon in signature_appearance
    - p12signature: str, path of the P12 file
    - password: str, password of the P12 file
    - flname: str, path of the target PDF
    - page: int, target page number
    - reason: str, reason of signing the document(OPTIONAL)
    """
    print("File: ", flname)
    date = datetime.datetime.utcnow()
    date = date.strftime("%Y%m%d")

    dct = {
        "aligned": 0,
        "sigflags": 3,
        "sigflagsft": 132,
        "sigpage": page,  # change this for per page implementation
        "sigbutton": True,
        "sigfield": "Signature1",
        "auto_sigfield": True,
        "sigandcertify": False,
        "signform": False,
        "signaturebox": (x, x1, y, y1),
        "signature_appearance": {
            "outline": [0.01, 0.02, 0.02],
            "icon": pdfimage,
            "labels": True,
            "display": f"{'CN'.split(',')}\n{'date'.split(',')}",
        },
        "contact": "mak@trisoft.com.pl",
        "location": "Szczecin",
        "signingdate": date,
        "reason": reason,
        "password": password,
    }
    bs = b""
    with open(p12signature, "rb") as fp:
        p12 = pkcs12.load_key_and_certificates(
            fp.read(), bs + password.encode("utf-8"), backends.default_backend()
        )
    print(p12[0], p12[1], p12[2])

    # if len(sys.argv) > 1:
    fname = flname

    print("File Path: ", fname)
    datau = open(fname, "rb").read()
    datas = pdf.cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")
    # fname = fname.replace(".pdf", "-signed-cms.pdf")
    with open(fname, "wb") as fp:
        fp.write(datau)
        fp.write(datas)
