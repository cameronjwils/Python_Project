from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_blueprint = Blueprint("city", __name__)

@city_blueprint.route("/bucket-list")
def city():
    cities = city_repository.select_all()
    return render_template("bucket-list/index.html", all_cities=cities)

@city_blueprint.route("/city/add", methods=['GET'])
def add_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)

@city_blueprint.route("/city", methods=['POST'])
def create_city():
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    visited = bool(int(request.form['visited']))
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/bucket-list')

