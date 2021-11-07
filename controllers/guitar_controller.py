from flask import Flask, render_template
from flask import Blueprint
from models.guitar import Guitar
import repositories.guitar_repository as guitar_repository

guitars_blueprint = Blueprint("guitars", __name__)

@guitars_blueprint.route("/Guitars")
def guitars():
    guitars = guitar_repository.select_all() 
    return render_template("guitar/index.html", guitars = guitars)