from db.run_sql import run_sql

from models.guitar import Guitar
# from models.manufacturer import Manufacturer

def save(guitar):
    sql = "INSERT INTO guitars (guitar_name,colour,manufacturer_id,guitar_type,no_of_strings,production_date,stock_price,selling_price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [guitar.guitar_name,guitar.colour,guitar.manufacturer.id,guitar.guitar_type,guitar.no_of_strings,guitar.production_date, guitar.stock_price,guitar.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    guitar.id = id
    return guitar

def select_all():
    guitars = []

    sql = "SELECT * FROM guitars"
    results = run_sql(sql)

    for row in results:
        guitar = Guitar(row['guitar_name'],row['colour'],row['manufacturer_id'],row['guitar_type'],row['no_of_strings'],row['production_date'],row['stock_price'],row['selling_price'])
        guitars.append(guitar)
    return guitars    