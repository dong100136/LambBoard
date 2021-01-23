'''
Author: jiandong.ye
email: yejiandong@bytedance.com
Date: 2020-12-23 23:32:55
description: 
'''
from flask import Flask
from pprint import pprint
from pathlib import Path
import logging
from collections import defaultdict
import json
app = Flask(__name__)

def load_exp_data():
    with open("../data/example.json",'r') as f:
        data = json.load(f)
    return json.dumps(data)

@app.route("/api/exp")
def get_all_exps():
    data = load_exp_data()
    return data

@app.route("/api/exp/<exp_name>")
def get_exp_metrics(exp_name):
    path = Path("../data/{}".format(exp_name))
    print("loading metrics data [{}]".format(path))

    metrics = defaultdict(list)
    for file in path.glob("*.metrics"):
        with open(file, 'r') as f:
            for line in f:
                p = json.loads(line)
                metric_name = p['name']
                metrics[metric_name].append(p)
    return json.dumps(metrics)


@app.route('/')
def hello_world():
    data = []
    with open("../data/run-tw_vlbert_ctr_0.5b-tag-Train-Loss.csv", 'r') as f:
        f.readline()
        for line in f:
            data.append(eval(line))
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7878')