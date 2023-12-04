import csv
from pathlib import Path

dataFile = 'notes.csv'
cfgFileDirectory = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(dataFile)


def get_notes():
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skipping the first row
        data = [tuple(row) for row in reader]
    return data
