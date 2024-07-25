import signature

pdfimg = "signaturetest.png"
p12signature = "SUGAR_RAY_B._RASONABLE_2021.p12"
password = "Rasonable2021"
pdfpath = "test.pdf"
pdfpaths = "test4.pdf"
search_word = "ADMIN H. USERNAME"


signature.single_sign(pdfimg, p12signature, password, pdfpath, search_word)
