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
    owners = owner_repository.select(id)
    return render_template("/owners/show.html", owners=owners)
