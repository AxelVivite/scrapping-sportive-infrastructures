from OverpassAdmin import OverpassAdmin
from os.path import exists
from time import sleep
import json

class SportsInfra(OverpassAdmin):
    def __init__(self, admin_level, country, name=None):
        super().__init__()
        self.filepath = f'./data/{country}/' if name is None else f'./data/{country}/{name}/'
        self.filename = f'sports-infra'
        name = country if name is None else name
        self.query = f"""
            [out:json];
            area["admin_level"="{admin_level}"]["name:en"="{name}"]->.searchArea;
            (
                node["leisure"="sports_centre"](area.searchArea);
                node["leisure"="stadium"](area.searchArea);
                node["leisure"="pitch"](area.searchArea);
                node["leisure"="track"](area.searchArea);
                node["leisure"="swimming_pool"](area.searchArea);
                node["leisure"="fitness_centre"](area.searchArea);
                node["sport"](area.searchArea);
                
                way["leisure"="sports_centre"](area.searchArea);
                way["leisure"="stadium"](area.searchArea);
                way["leisure"="pitch"](area.searchArea);
                way["leisure"="track"](area.searchArea);
                way["leisure"="swimming_pool"](area.searchArea);
                way["leisure"="fitness_centre"](area.searchArea);
                way["sport"](area.searchArea);
                
                relation["leisure"="sports_centre"](area.searchArea);
                relation["leisure"="stadium"](area.searchArea);
                relation["leisure"="pitch"](area.searchArea);
                relation["leisure"="track"](area.searchArea);
                relation["leisure"="swimming_pool"](area.searchArea);
                relation["leisure"="fitness_centre"](area.searchArea);
                relation["sport"](area.searchArea);
            );
            out body;
            """
        self.process()

    def filter_data(self):
        """
        Filter data to only list the elements
        """
        data = []

        for element in self.data:
            if 'tags' in element:
                element_tmp = element['tags'].copy()
                if 'lat' in element:
                    element_tmp['lat'] = element['lat']
                if 'lon' in element:
                    element_tmp['lon'] = element['lon']
                if 'nodes' in element:
                    element_tmp['geo_nodes'] = element['nodes']
                data.append(element_tmp.copy())
        self.data = data

    def process(self):
        """
        Process the data initialization and add it to a file
        """
        filename_raw = 'raw-' + self.filename + '.json'
        if exists(self.filepath + filename_raw):
            with open(self.filepath + filename_raw) as file:
                self.data = json.load(file)
            print(f'{self.filepath}{filename_raw} skipped')
        else:
            sleep(self.sleepDuration)
            self.query_overpass()
            self.data = self.data['elements']
            self.save_to_file(filename_raw)
            print(f'{self.filepath}{filename_raw} done')

        filename = self.filename + '.json'
        if exists(self.filepath + filename):
            with open(self.filepath + filename) as file:
                self.data = json.load(file)
            print(f'{self.filepath}{filename} skipped')
        else:
            self.filter_data()
            self.save_to_file(filename)
            print(f'{self.filepath}{filename} done')
