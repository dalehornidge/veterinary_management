from flask import Flask, render_template

from controllers.vets_controller import vets_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.pets_controller import pets_blueprint
import repositories.vet_repository as vet_repository
from models.vet import Vet

app = Flask(__name__)

app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(pets_blueprint)

@app.route("/")
def main():
    vets = vet_repository.select_all()
    return render_template('/vets/index.html', vets=vets)




if __name__ == '__main__':
    app.run