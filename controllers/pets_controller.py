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