import pdb

from models.vet import Vet
from models.owner import Owner
from models.pet import Pet

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository

owner_repository.delete_all()
vet_repository.delete_all()
pet_repository.delete_all()

vet1 = Vet("Gillian McAdams", "gillian@albavets.com", "07913432962")
vet_repository.save(vet1)

vet2 = Vet("Daniel Evans", "daniel@albavets.com", "07913442962")
vet_repository.save(vet2)

owner1 = Owner("Cara Forbes", "9/3 Ediburgh Road, Edinburgh, EH1 1FS", "07966656452", "requires assistance at entrance")
owner_repository.save(owner1)

owner2 = Owner("Martin Mackay", "49 Chemistry Lane, Edinburgh, EH3 5FH", "07969266452", "Prefers home visits")
owner_repository.save(owner2)

pet1 = Pet("Dobby", "26/11/2020", "dog", "Dobby is", owner1.id, vet1.id)
pet_repository.save(pet1)
pet2 = Pet("Ted", "18/04/2020", "cat", "Ted is shy", owner2.id, vet2.id)
pet_repository.save(pet2)


# print(owner_repository.select_all())
# print(pet_repository.select_all())
# print(vet_repository.select_all())

# owner_repository.select(owner1.id)
# pdb.set_trace()
