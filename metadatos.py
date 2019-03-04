#!/usr/bin/python
# -*- encoding: utf-8 -*- 

from PyPDF2 import PdfFileReader, PdfFileWriter # importamos modulo y librerias
import os 
import sys
from termcolor import colored, cprint

def printMeta(target):
	if not os.path.isdir(target):
		print "The directory no exists."
		return
	walk = os.walk(target)	
	for dirpath, dirnames, files in walk:
		for name in files:
			ext = name.lower().rsplit(".", 1)[-1]
			file_full_path = dirpath+os.path.sep+name
			if ext in ['pdf']:
				print_pdf(file_full_path)

def print_pdf(file_full_path):
 	# Header with file path
    cprint("[+] Metadata for file: %s " %(file_full_path), "green", attrs=['bold']) 
    # Open the file
    pdf_file = PdfFileReader(file(file_full_path, 'rb'))
    # Create a dictorionary with the info
    pdf_info = pdf_file.getDocumentInfo()
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
    # Print other info 
    cprint("\t Number of pages: %s" %pdf_file.getNumPages(), 'cyan')
    cprint("\t Is Encripted: %s" %pdf_file.getIsEncrypted(), 'cyan')
	
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
