from db.run_sql import run_sql
from models.owner import Owner
from models.vet import Vet


# save ///
# show all
# show by id
# delete all ////
# delete by id ////

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(owner):
    sql = "INSERT INTO owners (name, address, phone, owner_notes) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.name, owner.address, owner.phone, owner.owner_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for result in results:
        owner = Owner(result["name"], result["address"], result["phone"], result["owner_notes"], result["id"])
        owners.append(owner)
    return owners
