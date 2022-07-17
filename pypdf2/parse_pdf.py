import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
from tqdm import tqdm
import json
import os
import sys

def convert_to_json(pdfReader, id):
    pdfInfo = {}
    pdfInfo["id"] = id
    sents = [] 
    loc = []
    for i in range(0,pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        text = pageObj.extract_text()
        sentences = sent_tokenize(text.replace('\n', ''))
        for id,sent in enumerate(sentences):
            sents.append(word_tokenize(sent))
            loc.append(str(i+1)+'#'+str(id+1))
    pdfInfo["sents"] = sents
    pdfInfo["loc"]=loc
    return pdfInfo


def parse_pdf(inputFolder, outputFolder):
    for subdir, dirs, files in os.walk(inputFolder):
        for f in files:
            if f.endswith(".pdf"):
                pdfFileObj = open(os.path.join(subdir, f), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
                id = f.split('.')[0]
                pdfInfo = convert_to_json(pdfReader, id)
                path_to_json = os.path.join(outputFolder, id + ".json")
                with open(path_to_json, "w", encoding="utf-8") as writeJsonfile:
                    json.dump(pdfInfo, writeJsonfile, indent=4,default=str)

def main():
    try:
        inputFolder = sys.argv[1]
        outputFolder = sys.argv[2]
        parse_pdf(inputFolder, outputFolder)
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <inputFolder> <outputFolder>")

if __name__ == "__main__":
    main()


