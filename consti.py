import os
import json
from PyPDF2 import PdfFileReader

# Name variables
file_path = '/Country/file_name.pdf'
path_folder = '/Country/'
file_name="Constitution"

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

    # Write to markdown
    with open(os.path.join(path_folder, '{}.md'.format(file_name)), mode='w') as md_file:
        json.dump(full_text, md_file, indent=2)


# Call function
text_extractor(file_path)
