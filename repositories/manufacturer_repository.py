from db.run_sql import run_sql

from models.guitar import Guitar
from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (company_name,founded,location) VALUES (%s,%s,%s) RETURNING *"
    values = [manufacturer.company_name,manufacturer.founded,manufacturer.location]
    results = run_sql(sql,values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['company_name'],row['founded'],row['location'])
        manufacturers.append(manufacturer)
    return manufacturers
