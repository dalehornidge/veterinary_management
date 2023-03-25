from db.run_sql import run_sql
from models.owner import Owner
from models.vet import Vet


# save
# show all
# show by id
# delete all
# delete by id


def save(owner):
    sql = "INSERT INTO owners (name, address, phone, owner_notes) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.name, owner.address, owner.phone, owner.owner_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner


