from OverpassAdmin import OverpassAdmin

class States(OverpassAdmin):
    def __init__(self, country):
        super().__init__()
        self.filepath = f'./data/{country}/'
        self.filename = f'states.json'
        self.query = f"""
            [out:json];
            area["admin_level"="2"]["name:en"="{country}"]->.countryArea;
            (
                relation["admin_level"="4"](area.countryArea);
            );
            out body;
            """
        self.process()

    def filter_data(self):
        """
        Filter data to list only states names without duplicates and alphabetically
        """
        data = []

        for element in self.data['elements']:
            if 'tags' in element and 'name:en' in element['tags']:
                data.append(element['tags']['name:en'])
        data = list(dict.fromkeys(data))
        self.data = sorted(data)
