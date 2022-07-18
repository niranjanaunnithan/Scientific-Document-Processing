This folder contains scripts for extracting text from scholarly documents using s2orc-doc2json tool

# To convert pdf files to s2orc json format:

Steps:

1) Set up s2orc-doc2json and run grobid server. (https://github.com/allenai/s2orc-doc2json)

2) Run script run_s2orc_doc2json.py

Usage:

python run_s2orc_doc2json.py -i <input_path> -o <output_path>

# To extract specific sections of scholarly documents from json file:

Run script extract_data_from_json.py

Usage:

python extract_data_from_json.py -s <section_name> -i <input_path> -o <output_path>

Possible section names:

abstract

body

references