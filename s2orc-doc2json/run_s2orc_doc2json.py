import os
import time
import argparse

def run_s2orc_doc2json(inputFolder, outputFolder):
    for subdir, dirs, files in os.walk(inputFolder):
        for f in files:
            if f.endswith(".pdf"):
                inputPath = os.path.join(subdir, f)
                outputSubdir = subdir[-6:]
                outputPath = outputFolder + outputSubdir
                command = "python s2orc-doc2json/doc2json/grobid2json/process_pdf.py -i " + inputPath + " -t temp/ -o " + outputPath
                os.system(command)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run s2orc-doc2json tool")
    parser.add_argument("-i", "--input", default=None, help="path to the input directory containing PDF files")
    parser.add_argument("-o", "--output", default=None, help="path to the output dir for putting json files")

    args = parser.parse_args()

    inputPath = args.input
    outputPath = args.output

    startTime = time.time()

    run_s2orc_doc2json(inputPath, outputPath)

    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f"The time taken is {elapsedTime} seconds")