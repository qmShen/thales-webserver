# StationId, StationName, StationMap
import json

class DataService:
    def __init__(self, configPath):
        self.config_path = configPath
        self.init_config()

    def init_config(self):
        with open(self.config_path, 'r') as configFile:
            schemaString = configFile.readline()
            schemas = schemaString.split(',')
            schemas = [e.strip() for e in schemas]
            line = configFile.readline()
            self.station_config = []
            while line:
                elements = [e.strip() for e in line.split(',')]
                station_obj = {}
                for i in range(len(schemas)):
                    station_obj[schemas[i]] = elements[i]
                self.station_config.append(station_obj)

                line = configFile.readline()


    def get_map(self, station_id):
        map_path = None
        for obj in self.station_config:
            if obj['StationId'] == station_id:
                map_path = obj['StationMap']

        if map_path == None:
            print('No station_id', station_id, 'is found')
            return None

        with open(map_path, 'r') as map_file:
            map = json.load(map_file)
            map['stationId'] = station_id
            return map

    def get_legend_config(self, station_id):
        config_path = None
        for obj in self.station_config:
            if obj['StationId'] == station_id:
                config_path = obj['LegendConfig']

        if config_path == None:
            print('No station_id', station_id, 'is found')
            return None

        with open(config_path, 'r') as map_file:
            legend_config = json.load(map_file)
            return {
                'stationId': station_id,
                'legendConfig': legend_config
            }