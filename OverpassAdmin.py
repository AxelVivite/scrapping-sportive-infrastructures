from pathlib import Path
from os.path import exists
from time import sleep
import json
import requests

class OverpassAdmin():
    def __init__(self):
        self.data = []
        self.filename = 'untitled.json'
        self.filepath = './data/'
        self.query = ''
        self.sleepDuration = 1

    def query_overpass(self) -> dict:
        """
        Query the data
        """
        url = 'https://overpass-api.de/api/interpreter'
        response = requests.get(url, params={'data': self.query})
        response.raise_for_status()
        self.data = response.json()

    def save_to_file(self, filename=None):
        """
        Save data to a JSON file
        """
        filename = self.filename if filename is None else filename

        Path(self.filepath).mkdir(parents=True, exist_ok=True)
        with open(self.filepath + filename, 'w', encoding='utf8') as file:
            json.dump(self.data, file, indent=2, ensure_ascii=False)

    def filter_data(self):
        """
        Filter the data
        """
        pass

    def process(self):
        """
        Process the data initialization and add it to a file
        """
        if exists(self.filepath + self.filename):
            with open(self.filepath + self.filename) as file:
                self.data = json.load(file)
            print(f'{self.filepath}{self.filename} skipped')
            return
        sleep(self.sleepDuration)
        self.query_overpass()
        self.filter_data()
        self.save_to_file()
        print(f'{self.filepath}{self.filename} done')
        