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
    owner_notes TEXT
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    treatment_notes TEXT,
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) 
);


INSERT INTO owners (name, address, phone, owner_notes)
VALUES ('Unassigned Owner', 'Vet Practice', '0130115102', 'This animal has no owner assigned');

INSERT INTO owners (name, address, phone, owner_notes)
VALUES ('Jennifer Mclean', 'Vet Practice', '0130115102', 'Requires invoices printed');

INSERT INTO owners (name, address, phone, owner_notes)
VALUES ('Cara Burke', 'Vet Practice', '0130115102', 'Requires assistance at door');

INSERT INTO owners (name, address, phone, owner_notes)
VALUES ('Hillary Rodham', 'Vet Practice', '0130115102', 'Home visits required');


INSERT INTO vets (name, email, phone)
VALUES ('Gillian McDonald', 'gillian@alba.com', '0130115102');

INSERT INTO vets (name, email, phone)
VALUES ('Shaaista Bhutta', 'shaaista@alba.com', '0130115102');

INSERT INTO vets (name, email, phone)
VALUES ('Kate Byrnes', 'kate@alba.com', '0130115102');

INSERT INTO vets (name, email, phone)
VALUES ('Steffan Peston', 'steffan@alba.com', '0130115102');
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Dobby', '26/8/2020', 'dog', 'Dobby is a shy dog', 2, 1);
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Ted', '26/8/2020', 'dog', 'Ted is anxious', 2, 2);
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Theo', '26/8/2020', 'dog', 'Skin conditions reported', 3, 1);
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Jazz', '26/8/2020', 'cat', 'New to practice', 2, 4);
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Lucy', '26/8/2020', 'cat', 'Left paw injured', 3, 2);
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Sparky', '26/8/2020', 'dog', 'Finishing on medication', 1, 4);
INSERT INTO pets (name, dob, type, treatment_notes, owner_id, vet_id)
VALUES ('Henry', '26/8/2020', 'dog', 'Henry can be aggressive', 1, 1);



 