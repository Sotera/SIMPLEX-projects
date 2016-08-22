from flask import Flask, request
import os
import csv
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main_page():

 # Read in supplied data and write to disk
 data = request.form.to_dict()
 filename = "/opt/shiny-server/samples/sample-apps/BaylorInteractiveViewer/www/data/database.json"
 with open(filename, "w") as f:
  #f.write(data["graph"])
  for line in data["graph"].split("\n"):
   f.write(line +"\n")

 return "Data loaded"  

if __name__ == "__main__":
 app.run(debug=True, host="0.0.0.0")
