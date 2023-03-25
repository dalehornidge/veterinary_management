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
    sql = "INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.dob, pet.type, pet.treatment_notes, pet.owner_id, pet.vet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet
    
def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)
