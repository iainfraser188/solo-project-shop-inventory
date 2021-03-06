from db.run_sql import run_sql

from models.guitar import Guitar
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.guitar_repository as guitar_repository

def save(guitar):
    sql = "INSERT INTO guitars (guitar_name,colour,manufacturer_id,guitar_type,no_of_strings,production_date,stock_price,selling_price,quantity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [guitar.guitar_name,guitar.colour,guitar.manufacturer.id,guitar.guitar_type,guitar.no_of_strings,guitar.production_date, guitar.stock_price,guitar.selling_price,guitar.quantity]
    results = run_sql(sql, values)
    id = results[0]['id']
    guitar.id = id
    return guitar

def select_all():
    guitars = []

    sql = "SELECT * FROM guitars"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        guitar = Guitar(row['guitar_name'],row['colour'],manufacturer,row['guitar_type'],row['no_of_strings'],row['production_date'],row['stock_price'],row['selling_price'],row['quantity'],row['id'])
        guitars.append(guitar)
    return guitars    

def select(id):
    guitar = None
    sql = 'SELECT *FROM guitars WHERE id = %s'
    values = [id]
    result = run_sql(sql,values)[0]
    
    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        guitar = Guitar(result['guitar_name'],result['colour'],manufacturer,result['guitar_type'],result['no_of_strings'],result['production_date'],result['stock_price'],result['selling_price'],result['quantity'],result['id'])
    return guitar    

def delete(id):
    sql = "DELETE FROM guitars WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM guitars"
    run_sql(sql)   

def update(guitar):
    sql = "UPDATE guitars SET (guitar_name,colour,manufacturer_id,guitar_type,no_of_strings,production_date,stock_price,selling_price,quantity) = (%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE id=%s"
    values = [guitar.guitar_name,guitar.colour,guitar.manufacturer.id,guitar.guitar_type,guitar.no_of_strings,guitar.production_date, guitar.stock_price,guitar.selling_price,guitar.quantity,guitar.id]
    run_sql(sql, values)


