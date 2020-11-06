import os
import json
from config import BASE_PATH


def read_json(filename):
    filepath = BASE_PATH + os.sep + 'data' + os.sep + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        datas = json.load(f).values()
        arrs = []
        for data in datas:
            arrs.append(tuple(data.values()))

        # print(arrs)
        return arrs


if __name__ == '__main__':
    read_json('variety_list.json')