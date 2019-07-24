import os
import json
import csv
from PyPDF2 import PdfFileReader


# Create list
full_text = []

# Create extractor function
def text_extractor(file_path): 
  
    # Creates a pdf File object of original pdf 
    pdfFileObj = open(file_path, 'rb') 
      
    # Creates a pdf Reader object 
    pdfReader = PdfFileReader(pdfFileObj) 
      
    # Extract text from each page and append to list
    for page in range(pdfReader.numPages): 
  
        pageObj = pdfReader.getPage(page) 

        pagetext = pageObj.extractText()

        full_text.append(pagetext)
    
    with open(os.path.join(path_folder, '{}.md'.format(file_name)), mode='w', encoding='utf8') as md_file:
        json.dump(full_text, md_file, indent=2, ensure_ascii=False)
        


file_path = input("Enter the pdf file path: ")
path_folder = input("Enter the destination path folder: ")
file_name = input("Enter the markdown file name: ")

# # Usage
text_extractor(file_path)
