from flask import Blueprint, Flask, redirect, render_template, request

from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository



pets_blueprint = Blueprint("pets", __name__)

# Index
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets)
    
# Show by ID
@pets_blueprint.route("/pets/<id>")
def show_pets(id):
    pet = pet_repository.select(id)
    return render_template("pets/show.html", pets=pets)

@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect ("/pets")

@pets_blueprint.route("/pets/new")
def new_pet():
    return render_template("/pets/new.html")

@pets_blueprint.route("/pets/new", methods=["POST"])
def create_pet():
    name = request.form["name"]
    dob = request.form["dob"]
    type = request.form["type"]
    treatment_notes = request.form["treatment_notes"]
    owner_id = request.form["owner_id"]
    vet_id = request.form["vet_id"]
    new_pet = Pet(name, dob, type, treatment_notes, owner_id, vet_id)
    pet_repository.save(new_pet)
    return redirect("/pets")

