from flask import Blueprint, Flask, redirect, render_template, request

from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository


owners_blueprint = Blueprint("owners", __name__)

# Index
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("/owners/index.html", owners=owners)
    
# Show by ID
@owners_blueprint.route("/owners/<id>")
def show_owners(id):
    owner = owner_repository.select(id)
    return render_template("/owners/show.html", owner=owner)


@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect ("/owners")

@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template ("owners/new.html")

@owners_blueprint.route("/owners/new", methods=["POST"])
def create_owner():
    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]
    owner_notes = request.form["owner_notes"]
    new_owner = Owner(name, address, phone, owner_notes)
    owner_repository.save(new_owner)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>/pets")
def show_pets(id):
    owner = owner_repository.select(id)
    pets = vet_repository.show_all(id)
    return render_template("owners/pets.html", pets=pets, owner=owner)


@owners_blueprint.route("/owners/<id>/edit", methods=["GET"])
def update_owner_get(id):
    owner = owner_repository.select(id)
    return render_template("/owners/edit.html", owner=owner)



@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update_owner(id):
    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]
    owner_notes = request.form["owner_notes"]
    owner = Owner(name, address, phone, owner_notes, id)
    owner_repository.update(owner)
    return redirect("/owners")
