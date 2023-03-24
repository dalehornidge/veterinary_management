DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;


CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(20),
    owner_notes TEXT,
    pet_id INT
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    treatment_notes TEXT,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

ALTER TABLE owners ADD CONSTRAINT fk_owners_pets FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE;
