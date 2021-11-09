from flask import Flask, render_template, redirect, request
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
    guitars = guitar_repository.select_all()
    return render_template("guitar/new.html", all_manufacturers = manufacturers, all_guitars=guitars)

@guitars_blueprint.route("/Guitars", methods = ['POST'])
def create_guitar():
    guitar_name = request.form['guitar_name']
    colour = request.form['colour']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    guitar_type = request.form['guitar_type']
    no_of_strings = request.form['no_of_strings']
    production_date = request.form['production_date']
    stock_price = request.form['stock_price']
    selling_price = request.form['selling_price']
    guitar = Guitar(guitar_name,colour,manufacturer,guitar_type,no_of_strings,production_date,stock_price,selling_price)
    guitar_repository.save(guitar)
    return redirect('/Guitars')
    

@guitars_blueprint.route("/Guitars/<id>/delete", methods=['POST','GET'])
def delete_guitar(id):
    guitar_repository.delete(id)
    return redirect('/Guitars')    

