import csv
import psycopg2
import re
from prediction.database import session, Entry

with open('pssa10year.csv') as csvfile:
    for row in csv.DictReader(csvfile):
        print(row)

tables = {
"entries": ("pssa10year.csv", "PAsecureID"),
}
