from OverpassAdmin import OverpassAdmin

class Countries(OverpassAdmin):
    def __init__(self):
        super().__init__()
        self.filename = 'countries.json'
        self.query = """
            [out:json];
            relation["admin_level"="2"];
            out body;
            """
        self.sleepDuration = 0
        self.process()

    def filter_data(self):
        """
        Filter data to list only countries names without duplicates and alphabetically
        """
        data = []
        blacklist = ['landmass',
                     'land mass',
                     '-', '—', '–',
                     'extent',
                     'eez', 'exclusive',
                     'territorial',
                     'zone', 'national',
                     'federal', 'territory',
                     'border', 'control',
                     'disputed', 'civil'
                     ]

        for element in self.data['elements']:
            if 'tags' in element and 'name:en' in element['tags'] and not any(text in element['tags']['name:en'].lower() for text in blacklist):
                data.append(element['tags']['name:en'])
        data = list(dict.fromkeys(data))
        self.data = sorted(data)
