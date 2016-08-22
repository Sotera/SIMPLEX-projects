from flask import Flask, request
import csv
import json

app = Flask(__name__)

@app.route("/")
def main_page():
 
 # Read in the csv into a dictionary and make it fancy ...
 #csvfile = open("ctd_hash.csv", "r")
 #fieldnames = ("entity1", "type1",  "entity2", "type2", "relation_type", "source", "entity1hash" "entity2hash")
 #reader = csv.DictReader(csvfile, fieldnames, delimiter=" ")
 #readr.next() # remove header
 #ctd = [row for row in reader]

 # Just store the text
 with open("ctd_hash.csv", "r") as f:
  ctd = "".join(f.readlines())

 tsvfile = open("GESA_Canonical_pathways_c2.cp.v5.0.symbols.gmt_filtered.tsv", "r")
 labels = {}
 for row in tsvfile:
  items = row.strip().split("\t")
  labels[items[0]] = items[1:]

 data = {'ctd':ctd, 'labels':labels}

 return json.dumps(data)


if __name__ == "__main__":
 app.run(debug=True, host="0.0.0.0")
