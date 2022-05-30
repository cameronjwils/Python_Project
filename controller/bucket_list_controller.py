from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

bucket_list_blueprint = Blueprint("bucket_list", __name__)

@bucket_list_blueprint.route("/bucket_list")
def bucket_list():
    cities = city_repository.select_all()
    return render_template("cities/show_cities.hmtl", all_cities = cities)