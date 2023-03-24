class Pet:
    def __init__(self, name, dob, type, treatment_notes, owner, vet, id=None):
        self.name = name
        self.dob = dob
        self.type = type
        self.treatment_notes = treatment_notes
        self.owner = owner
        self.vet = vet
        self.id = id