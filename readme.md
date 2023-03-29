# Veterinary Management App

👋 Welcome to my Veterinary Management App! 🐾

This web application is designed to help veterinary practices manage their pet clientele in a more efficient and streamlined manner. It was built using Python, Flask, HTML, and CSS, along with the pyscopg2 and PostgreSQL libraries to manage the SQL database.

## 🚀 Features

Here's what you can expect from my Veterinary Management App:

- A comprehensive overview of each patient with one-to-many relationships between clients, pets, and vets.
- An intuitive search function that allows users to search for client lists based on pet name or owner surname.
- The ability to save pet data, including treatment notes, to the SQL database, with full CRUD functionality for pets in the database.
- A clean, user-friendly interface that displays the pets owned by each owner.

## 🎨 Design Notes

I believe that a well-designed interface can make all the difference in the user experience. That's why I designed the front-end interface from scratch, using relatively simple CSS to generate a stylish and modern look. While the current database data is pre-populated using run_sql.py, the app is designed to handle new data added from scratch or imported from other sources.

## 🔧 Installation

To run my app locally, simply follow these steps:

1. Clone this repository using Git.
2. Create the database using the command "Createdb veterinary_management".
3. Create the database tables using the command "psql -d veterinary_management -f vet_manager.sql".
4. Run the app (ensure Flask has been uploaded beforehand) using the command "Flask run".

## 🤝 Contributing

As the sole developer of this app, I would love to hear your feedback! If you encounter a bug or have an idea for a new feature, please don't hesitate to open an issue or submit a pull request. I am always looking for ways to improve my app, and I welcome any and all feedback.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for more information.

Thank you for checking out my Veterinary Management App. 🐶🐱
