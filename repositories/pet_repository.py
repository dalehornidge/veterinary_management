from db.run_sql import run_sql
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet


# save ///
# show all
# show by id
# delete all ////
# delete by id ////

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(pet):
    sql = "INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.type, pet.treatment_notes, pet.owner_id, pet.vet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for result in results:
        pet = Pet(result["name"], result["dob"], result["type"], result["treatment_notes"], result["owner_id"], result["vet_id"], result["id"])
        pets.append(pet)
    return pets
