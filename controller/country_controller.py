from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_blueprint = Blueprint("country", __name__)

@country_blueprint.route("/countries")
def city():
    countries = country_repository.select_all()
    return render_template("countries/show.html", all_countries = countries)

@country_blueprint.route("/country/add", methods=['GET'])
def add_country():
    return render_template("countries/new.html")

@country_blueprint.route("/country", methods=['POST'])
def create_city():
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect('/cities')

@country_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/cities')