from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO countries (name, country) VALUES (?, ?) RETURNING *"
    values = [city.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city