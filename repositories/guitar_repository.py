from db.run_sql import run_sql

from models.guitar import Guitar
from models.manufacturer import Manufacturer

def save(guitar):
    sql = "INSERT INTO guitars (guitar_name,colour,manufacturer,guitar_type,no_of_strings,production_date,stock_price,selling_price,guitar_id) VALUES ($s,$s,$s,$s,$s,$s,$s,$s) RETURNING *"
    values = [guitar.guitar_name,guitar.manufacturer.id,guitar.guitar_type,guitar.no_of_strings,guitar.production_date, guitar.stock_price,guitar.selling_price]
    results = (sql, values)
    id = results[0]['id']
    guitar.id = id
    return guitar