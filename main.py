#Projet data mining

#if __name__ == '__main__':

import urllib.request

#urllib.request permet de lire les url. urlretrieve permet de les sauvegarder

urllib.request.urlretrieve('https://www.has-sante.fr/upload/docs/application/pdf/ct020974.pdf', "doliprane.pdf")
urllib.request.urlretrieve('https://www.bip31.fr/bip/BIP%202007,%2014,%20(2),%207-15.pdf', "spasfon.pdf")
urllib.request.urlretrieve('https://www.pharma-medicaments.com/media/3322661__007243700_1543_23042013.pdf', "strepsils.pdf")

fichier_doliprane = 'doliprane.pdf'
fichier_spasfon = 'spasfon.pdf'
fichier_strepsils = 'strepsils.pdf'




#! pip install PyPDF2

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

#Lecture du fichier sur le doliprane

document_doliprane = PdfFileReader(open(fichier_doliprane, 'rb'))

pdftext_doliprane = ""
for page in range(document_doliprane.numPages):
    pageObj = document_doliprane.getPage(page)
    pdftext_doliprane += pageObj.extractText()  # .replace('\n','')

print(pdftext_doliprane)

#Lecture du fichier sur le spasfon

document_spasfon = PdfFileReader(open(fichier_spasfon, 'rb'))

pdftext_spasfon = ""
for page in range(document_spasfon.numPages):
    pageObj = document_spasfon.getPage(page)
    pdftext_spasfon += pageObj.extractText().replace('\n','')

print(pdftext_spasfon)

#Lecture du fichier sur le strepsils

document_strepsils = PdfFileReader(open(fichier_strepsils, 'rb'))

pdftext_strepsils = ""
for page in range(document_strepsils.numPages):
    pageObj = document_strepsils.getPage(page)
    pdftext_strepsils += pageObj.extractText() #.replace('\n','')

print(pdftext_strepsils)

