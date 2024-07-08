#!/usr/bin/python3
# Lists all cities of the DB ordered by ID
# Usage ./4-cities_by_state.py <mysql username> \
# <mysql password> <mysql database name>

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`)
