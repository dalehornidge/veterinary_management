from db.run_sql import run_sql
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet


# save ///
# show all
# show by id
# delete all
# delete by id


def save(pet):
    sql = "INSERT INTO vets (name, email, phone) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.type, pet.treatment_notes, pet.owner, pet.vet]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet
    

