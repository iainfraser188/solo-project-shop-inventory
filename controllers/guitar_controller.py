from flask import Flask, render_template
from flask import Blueprint
from models.guitar import Guitar
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() 
    return render_template("manu.html", all_manufacturers = manufacturers)