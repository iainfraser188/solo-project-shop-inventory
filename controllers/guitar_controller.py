from flask import Flask, render_template
from flask import Blueprint
from controllers.manufacturer_controller import manufacturers
from models.guitar import Guitar
import repositories.guitar_repository as guitar_repository
import repositories.manufacturer_repository as manufacturer_repository

guitars_blueprint = Blueprint("guitars", __name__)

@guitars_blueprint.route("/Guitars")
def guitars():
    guitars = guitar_repository.select_all() 
    return render_template("guitar/index.html", guitars = guitars)

@guitars_blueprint.route("/Guitars/<id>",methods=['GET'] ) 
def show_guitar(id):
    guitar = guitar_repository.select(id) 
    return render_template('guitar/individual.html', guitar = guitar)  


@guitars_blueprint.route("/Guitars/new", methods=['GET'])
def new_guitar():
    manufacturers = manufacturer_repository.select_all()
    return render_template("guitar/new.html", all_manufacturers = manufacturers)
    

    