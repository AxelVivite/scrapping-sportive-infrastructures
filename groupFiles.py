import os
from pathlib import Path

def groupFiles(resultFilename, filenameToGroup):
    """
    Group all the files by filename from the data folder in a result file
    """
    Path('./data').mkdir(parents=True, exist_ok=True)
    with open('./data/' + resultFilename, 'w', encoding='utf8') as result:
        result.write('[\n')
        for dirpath, dirnames, filenames in os.walk("./data/"):
            for filename in filenames:
                if filename == filenameToGroup:
                    print(dirpath + filename)
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            if len(lines) > 3:
                                if line == lines[-2]:
                                    result.write(line[:-1] + ',\n')
                                elif line != lines[0] and line != lines[-1]:
                                    result.write(line)
        result.write(']')
