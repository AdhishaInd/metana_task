import sqlite3

from models.responseBodies import CompleteForm

class CRUD:
    def __init__(self):
        self.conn = sqlite3.connect('database/your_database.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS submissions
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        firstname TEXT,
                        lastname TEXT,
                        email TEXT UNIQUE,
                        country TEXT,
                        phonenumber TEXT,
                        experience TEXT,
                        compensation TEXT,
                        acknowledgement BOOLEAN,
                        linkedin TEXT,
                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS languages
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        language TEXT,
                        owner_id INTEGER,
                        FOREIGN KEY(owner_id) REFERENCES submissions(id))''')

    def insert_submission(self, form: CompleteForm):
        self.c.execute("INSERT INTO submissions (firstname, lastname, email, country, phonenumber, experience, compensation, acknowledgement, linkedin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (form.firstname, form.lastname, form.email, form.country, form.phonenumber, form.experience, form.compensation, form.acknowledgement, form.linkedin))
        submission_id = self.c.lastrowid

        for language in form.languages:
            self.insert_language(language, submission_id)

        return submission_id

    def insert_language(self, language, owner_id):
        self.c.execute("INSERT INTO languages (language, owner_id) VALUES (?, ?)", (language, owner_id))

    def get_submissions_count(self):
        self.c.execute("SELECT COUNT(*) FROM submissions")
        submissions_count = self.c.fetchone()[0]
        return submissions_count

    def close(self):
        self.conn.commit()
        self.conn.close()

# # Connect to the database
# conn = sqlite3.connect('database/your_database.db')
# c = conn.cursor()

# # Create a table
# c.execute('''CREATE TABLE IF NOT EXISTS submissions
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  firstname TEXT,
#                  lastname TEXT,
#                  email TEXT UNIQUE,
#                  country TEXT,
#                  phonenumber TEXT,
#                  experience TEXT,
#                  compensation TEXT,
#                  acknowledgement BOOLEAN,
#                  linkedin TEXT,
#                  time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# # Create another table
# c.execute('''CREATE TABLE IF NOT EXISTS languages
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  language TEXT,
#                  owner_id INTEGER,
#                  FOREIGN KEY(owner_id) REFERENCES submissions(id))''')

# # Insert a new submission
# c.execute("INSERT INTO submissions (firstname, lastname, email, country, phonenumber, experience, compensation, acknowledgement, linkedin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#           ('John', 'Doe', 'jhdj.doe@example.com', 'USA', '1234567890', '5 years', 'Negotiable', True, 'https://linkedin.com/in/johndoe'))

# # Get the ID of the newly inserted submission
# submission_id = c.lastrowid

# # Insert languages for the new submission
# c.execute("INSERT INTO languages (language, owner_id) VALUES (?, ?)", ('Python', submission_id))
# c.execute("INSERT INTO languages (language, owner_id) VALUES (?, ?)", ('JavaScript', submission_id))

# # Commit the changes
# conn.commit()

# # Get the count of submissions
# c.execute("SELECT COUNT(*) FROM submissions")
# submissions_count = c.fetchone()[0]
# print(f"Total submissions: {submissions_count}")

# # Close the connection
# conn.close()