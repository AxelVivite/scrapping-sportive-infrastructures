from Countries import Countries
from SportsInfra import SportsInfra
from States import States
from groupFiles import groupFiles

def main():
    """
    Create all the data folder stucture and .json files
    TODO: Add flags to force file refresh instead of skipping if file exist
    """
    dataset = []
    countries = Countries()
    for country in countries.data:
        states = States(country)
        dataset.append({'name': country, 'states': states.data})
    for country in dataset:
        if not country['states']:
            SportsInfra(2, country['name'])
        else:
            for state in country['states']:
                SportsInfra(4, country['name'], state)

    """
    Group all the .json files in two files
    TODO: Put the data in a noSQL dtb (MongoDB ?)
    """
    groupFiles('world-sports-infra.json', 'sports-infra.json')
    groupFiles('raw-world-sports-infra.json', 'raw-sports-infra.json')

if __name__ == "__main__":
    main()
