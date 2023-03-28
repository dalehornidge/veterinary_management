from flask import Blueprint, Flask, redirect, render_template, request

from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository


vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)
    
@vets_blueprint.route("/vets/<id>")
def show_vets(id):
    vets = vet_repository.select(id)
    return render_template("vets/show.html", vets=vets)

# New
@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template ("vets/new.html")

# # Create
# @vets_blueprint.route("/vets", methods=["POST"])
# def create_vet():
#     name 

@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect ("/vets")