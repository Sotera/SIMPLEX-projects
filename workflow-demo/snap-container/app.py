from flask import Flask, request
import os
import csv
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main_page():

 # Read in supplied data and write to disk
 data = request.form.to_dict()
 with open("ctd_hash.txt", "w") as f:
  f.write(data["ctd"])

 # Run SNAP's community detection (CNM)
 os.system("python recursive_community_iteration.py")

 # Return the output as JSON
 with open("current_graph.json", "r") as f:
  final_data = "".join((line for line in f))

 return json.dumps({"graph":final_data}) 

if __name__ == "__main__":
 app.run(debug=True, host="0.0.0.0")
