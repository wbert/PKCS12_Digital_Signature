import signature

pdfimg = "signaturetest.png"
p12signature = "SUGAR_RAY_B._RASONABLE_2021.p12"
password = "Rasonable2021"
# pdfpath = "dsd.pdf"
pdfpaths = ["test_case1.pdf", "test_case2.pdf"]
search_word = "ADMIN H. USERNAME"


signature.per_name_sign_batch(pdfimg, p12signature, password, pdfpaths, search_word)
