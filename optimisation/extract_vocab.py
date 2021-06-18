
import json

with open("roberta_vocab.txt") as json_file:
    data = json.load(json_file)

outfile = open("roberta.txt", "w")

for key, value in data.items():
    if (key[0]=="Ġ"):
        # print("true")
        outfile.write(key[1:].lower()+"\n")
    else:
        outfile.write(key.lower()+"\n")
  