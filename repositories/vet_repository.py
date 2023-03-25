from db.run_sql import run_sql
from models.vet import Vet


# save ///
# show all
# show by id
# delete all
# delete by id

def save(vet):
    sql = "INSERT INTO vets (name, email, phone) VALUES (%s, %s, %s) RETURNING id"
    values = [vet.name, vet.email, vet.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet
    

