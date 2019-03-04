
#!/usr/bin/python
# -*- encoding: utf-8 -*- 

from PyPDF2 import PdfFileReader, PdfFileWriter # importamos modulo y librerias
import os # importamos modulo os para ir a otras carpetas
import sys
from termcolor import colored, cprint

def printMeta(dir):
    if not os.path.exists(dir): # verifica que exista el directorio que vamos a escanear
        print "The directory no exists." 
        return
    for dirpath, dirnames, files in os.walk(dir):# para el diretorio, nombre y archivos en la carpeta dir
        for name in files:#recorremos los posibles ficheros'''
            ext = name.lower().rsplit('.', 1)[-1]
            file_full_path = dirpath+os.path.sep+name
            if ext in ['pdf']:
                print_pdf(file_full_path)
            if ext in ['docx']:
                print_docx(file_full_path)

def print_pdf(file_full_path):
    # Header with file path
    cprint("[+] Metadata for file: %s " %(file), "green", attrs=['bold']) 
    # Open the file
    pdf_file = PdfFileReader(file(file_full_path, 'rb'))
    # Create a dictorionary with the info
    pdf_info = pdfFile.getDocumentInfo()
    # Print metadata
    if pdf_info:
        for metaItem in pdf_info:
            try:
                cprint('\t ' + metaItem[1:] + ': ', 'cyan', end="")
                cprint(pdf_info[metaItem])
            except TypeError: 
                cprint('\t ' + metaItem[1:] + ': ' + 'Error - Item not redeable', 'red')
    else:
        cprint('Not data found', 'red')
    # Imprime más informacion del documento 
    cprint("\t- Number of pages: " + pdfFile.getNumPages() )
    cprint("\t- Fields:%s" %(pdfFile.getFields()))
    cprint("\t- is Encripted:%s" %(pdfFile.getIsEncrypted() ))
    print ""

def print_doc(file_full_path):

# Main function
def main(argv):
    # Check arguments
    if len(argv) != 2:
        print("Incorrect number of arguments.")
    # If arguments OK, execute function
    else: 
        target = argv[1]
        printMeta(target)

# Execute main function
if __name__ == "__main__": 
	main(sys.argv)
