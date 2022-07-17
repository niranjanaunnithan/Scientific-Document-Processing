This folder contains scripts for extracting text from scholarly documents using s2orc-doc2json tool

To extract specific sections of scholarly documents from json file:

Run script extract_data_from_json.py

Usage:

python extract_data_from_json.py -s <section_name> -i <input_path> -o <output_path>

Possible section names:
abstract
body
references