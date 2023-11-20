import json
from yaml import load,dump, Loader, Dumper
y = load(open("data/content.yaml",encoding="utf8"),Loader=Loader)
f = open ("data/content2.json","w")
json.dump(y,f)
