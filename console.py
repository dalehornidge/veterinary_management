import pdb

from models.vet import Vet
from models.owner import Owner
from models.pet import Pet

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

vet1 = Vet("Gillian McAdams", "gillian@albavets.com", "07913432962")
vet_repository.save(vet1)

vet2 = Vet("Daniel Evans", "daniel@albavets.com", "07913442962")
vet_repository.save(vet2)

owner1 = Owner("Cara Babineau", "9/3 Ediburgh Road, Edinburgh, EH1 1FS", "07966656452", "requires assistance at entrance")
owner_repository.save(owner1)

pet1 = Pet("Dobby", "26/11/2020", "dog", "Dobby is friendly", owner1, vet1)





#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     dob VARCHAR(255),
#     type VARCHAR(255),
#     treatment_notes TEXT,
#     owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
#     vet_id INT REFERENCES vets(id) ON DELETE CASCADE
