class Pet:
    def __init__(self, name, dob, type, treatment_notes, owner_id, vet_id, id=None):
        self.name = name
        self.dob = dob
        self.type = type
        self.treatment_notes = treatment_notes
        self.owner_id = owner_id
        self.vet_id = vet_id
        self.id = id