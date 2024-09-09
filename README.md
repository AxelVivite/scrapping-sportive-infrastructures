# SI Query

SI Query or sportive infrastructures Query retrieve from OpenStreetMap (OverpassAPI) all the sportive infractures in the world.

## Description

On start, the program will start retrieving data from the OverpassAPI.
It start by requesting all the Countries in the world (Overpass Admin zone level 2).
The it retrieve every states from those countries (Overpass Admin zone level 4).
And finally, every sportive infrastructures of every states are requested.

## Getting Started

### Installing

Clone the project on your computer.

In VsCode:
* Open the VsCode prompt: Ctrl + Shift + P
* Select in the prompt: "Python: create environment"
* Select: "Venv"
* Select: "Python 3.x"

On a Linux Terminal:
* Open a terminal
* Navigate to the project (cd)
* Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

### Dependencies

On a terminal (open one in VsCode):
```
python3 -m pip install -r requirements.txt
```

### Executing program

In VsCode:
* Open the file "main.py"
* Press the button "Run Python File"

On a terminal:
```
python3 main.py
```

## Help

Flags are coming in next updates.
The command would be:
```
python3 main.py --help
```
or
```
python3 main.py -h
```

## Authors

[Axel Virot](axel.virot@gmail.com)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [Overpass Turbo](https://overpass-turbo.eu/)
