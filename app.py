import os
from typing import Dict
from flask import Flask, request


_cwd = os.getcwd()
app = Flask(__name__)


def from_ymd_to_mdy_date_format(date: str) -> str:
    year, month, day = date.split('-')
    return '-'.join([month, day, year])


def from_mdy_to_ymd_date_format(date: str) -> str:
    month, day, year = date.split('-')
    return '-'.join([year, month, day])


def read_data(week_start: str, week_end: str) -> Dict[str, int or str]:   # LOL int or str we can do it and it won't crack? 
    path = os.path.join(_cwd, 'data')
    filename = os.path.join(path, week_start + '_' + week_end + '.csv')

    with open(filename, 'r') as file:
        lines = file.readlines()
        data = dict()

        for line in lines:
            key, value = line.split(',')
            if '-' not in value:
                data[key] = int(value.strip())
            else:
                data[key] = from_mdy_to_ymd_date_format(value.strip())

        return data


@app.route('/data', methods=['GET'])
def data_endpoint():
    if request.method == 'GET':
        week_start = request.args.get('week_start')
        week_end = request.args.get('week_end')

        if week_end and week_start:
            try:
                data = read_data(from_ymd_to_mdy_date_format(week_start), from_ymd_to_mdy_date_format(week_end))
            except FileNotFoundError:
                return {"message": "Wrong parameters"}, 404
            else:
                return data
        return {'message': 'Wrong number of parameters'}, 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
