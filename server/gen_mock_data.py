'''
Author: your name
Date: 2021-01-23 14:04:01
LastEditTime: 2021-01-23 16:26:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /vuetify-todo-pwa/Users/bytedance/projects/private/vue-test/server/gen_mock_data.py
'''
import numpy as np
import pandas as pd
import time
import json


def gen_mock_data(name, path):
    data = []
    for i in range(0, 100):
        point = {
            'step': i,
            'timestamp': time.time(),
            'name':name,
            'value': 3 - np.log((i + 1) / 10) + np.random.rand()
        }

        data.append(point)

    with open(path, 'w') as f:
        for line in data:
            f.write(json.dumps(line))
            f.write('\n')

if __name__ == '__main__':
   gen_mock_data('loss', '../data/resnet/loss.metrics')
   gen_mock_data('train/acc', '../data/resnet/train_acc.metrics')

   gen_mock_data('loss', '../data/vlbert/loss.metrics')
   gen_mock_data('train/acc', '../data/vlbert/train_acc.metrics')

