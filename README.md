# PKCS12 Digital Signature

PKCS #12, also known as PFX, is a standard format for securely bundling and exchanging cryptographic keys and certificates in a single encrypted file. It typically includes a private key and the corresponding public key certificate, protected by a password. This format is widely used for transferring cryptographic information and is essential in applications involving digital signatures, where the private key is used to sign data and the public key certificate is used for signature verification.

### Requirements

- PDF document must be Optical Character Recongiton(OCR)
- Image of the signature in a `.png` format without background
- PKCS12 file is required

### Dependencies

This is a combination of two dependencies, [endesive](https://pypi.org/project/endesive/) and [pdfminer](https://pypi.org/project/pdfminer.six/).

### Execution

- The pdfminer extracts the contents and the coordinates of the texts inside the PDF file.
- Retrieve all the texts and coordinates from pdfminer.
- Select the coordinates you are going to target based on the requirements.
- Execute endesive to sign and serialize the document.

### Installation

###### Init venv

Initialize virtual environment <br/>
`python -m venv myenv`
or
`python3 -m venv myenv`

##### Install Requirements

`pip install requirements.txt`

### Usage

`signature.single_sign`
<br>
Signs only the last instance of the word you are trying to search on the last page of the PDF file.
<img width="1441" alt="image" src="https://github.com/user-attachments/assets/2962680d-fead-4b2d-9e42-451f42e1d209">

`signature.per_page_sign`
<br>
Signs the last instance of the word you are trying to search on every page of the PDF file.
<img width="1441" alt="image" src="https://github.com/user-attachments/assets/f30048c0-6219-41d0-9194-48dad85d3f17">

`signature.multiple_sign`
Works the same as `signature.single_sign` but instead of passing a single file path, you are required to pass an array of file paths to sign multiple PDFs at a time.

### Wrapping Up

This is still not polished, but if you are willing to contribute, feel free to do so!
