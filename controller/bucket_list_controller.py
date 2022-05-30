from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

bucket_list_blueprint = Blueprint("bucket_list", __name__)

@bucket_list_blueprint.route("/bucket-list")
def bucket_list():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities=cities)

@bucket_list_blueprint.route("/city/add", methods=['GET'])
def add_city():
    countries = country_repository.select_all()
    return render_template("cities/add.html")

@bucket_list_blueprint.route("/city", methods=['POST'])
def create_city():
    name = request.form['name']
    country = request.form['country']
    visited   = bool(int(request.form['visited']))
    city = City(name, country)
    city_repository.save(city)
    return redirect('/bucket-list')

