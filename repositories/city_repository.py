from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (?, ?) RETURNING *"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['country_id'],row['id'] )
        cities.append(city)
    return cities

def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE books SET (name, country_id) = (?, ?) WHERE id = ?"
    values = [city.name, city.country.id, city.id]
    print(values)
    run_sql(sql, values)