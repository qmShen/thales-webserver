# -*- coding: UTF-8 -*-
from app import app
import json
from app.DataService.DataService import DataService
from flask import request


dataService = DataService('config.txt')
print('here')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/test')
def getStationConfig():
    return json.dumps("test")

@app.route('/getStationMap',  methods = ['POST'])
def get_map():
    print('test')
    post_data = json.loads(request.data.decode())
    station_id = post_data['StationId']
    map = dataService.get_map(station_id)
    return json.dumps(map)

@app.route('/getLegendConfiguration',  methods = ['POST'])
def get_legend_config():
    print('Config')
    post_data = json.loads(request.data.decode())
    station_id = post_data['StationId']
    config = dataService.get_legend_config(station_id)
    return json.dumps(config)




if __name__ == '__main__':
    pass