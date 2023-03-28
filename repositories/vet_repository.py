from db.run_sql import run_sql
from models.vet import Vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(vet):
    sql = "INSERT INTO vets (name, email, phone) VALUES (%s, %s, %s) RETURNING id"
    values = [vet.name, vet.email, vet.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet
    
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for result in results:
        vet = Vet(result["name"], result["email"], result["phone"], result["id"])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        vet = Vet(result['name'], result['email'], result['phone'], result['id'])
    return vet

