from flask import Flask, render_template
import os
import random
import json
import math
app = Flask(__name__)

rootdir = '/Users/ziv/GDrive/papers'
papers = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	f = os.path.join(subdir, file)
    	if f.split('/')[-1][0] != "." and f.split('/')[5] != "app":
    		papers.append(f)

def path_to_dict(path):
    name = os.path.basename(path)
    if name == "app":
        pass
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path) if x[0] != '.' and name != 'app']
    else:
        d['type'] = "file"
        d['size'] = os.stat(path).st_size
    return d

data = json.dumps(path_to_dict('/Users/ziv/GDrive/papers'))

# with open('flare.json') as data_file:    
#     data = json.load(data_file)

@app.route("/")
def index():
	print data
	return render_template('index.html', papers=map(lambda x: x[25:], papers), lpap = len(papers), data=data)

if __name__ == "__main__":
    app.run(debug=True)