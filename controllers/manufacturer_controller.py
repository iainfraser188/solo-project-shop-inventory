from flask import Flask, render_template,redirect, request
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.guitar_repository as guitar_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() 
    return render_template("manufacturer/index.html", all_manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>", methods = ['get'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    # guitars = guitar_repository.select_by_company(manufacturer)
    return render_template('manufacturer/individual.html', manufacturer = manufacturer)

 
@manufacturers_blueprint.route("/manufacturers/<id>/delete",methods=['POST','GET'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')
     
@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturer/new.html",  manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
       manufacturer_name=request.form['manufacturer_name']
       established=request.form['established']
       location=request.form['location'] 
       manufacturer=Manufacturer(manufacturer_name,location,established)
       manufacturer_repository.save(manufacturer)
       return redirect('/manufacturers')