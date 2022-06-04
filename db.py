from ast import Pass
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

connection = mysql.connector.connect( host = HOST, port=PORT, user = USERNAME, password = PASSWORD)
cursor = connection.cursor()
cursor = connection.cursor(buffered=True)

def create_db(db_name: str) -> None:
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print("Database created successfully")
        
    except:
        print("Database already exists, dropping it and creating from scratch!")
        cursor.execute(f"DROP DATABASE {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")
        print("Database created successfully")


def create_table(query: str) -> None:
    cursor.execute(query)
    connection.commit()
    print("Created table successfully")


def insert_data(query: str) -> None:
    cursor.execute(query)
    connection.commit()
    print("Inserted data successfully")


def fetch_data(query) -> list:
    fetch_cursor = cursor.execute(query)
    fetched_data = cursor.fetchall()
    connection.commit()

    return fetched_data

create_db("test_db")
# create tables
query = """
    CREATE TABLE test_db.Course(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(40),
        release_year DATE,
        direction VARCHAR(40)
    )
    """

create_table(query)

query2 = """

CREATE TABLE test_db.Student(
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    date_of_birth DATE,
    course_id INT,
    FOREIGN KEY(course_id) REFERENCES Course(id) )
"""
create_table(query2)

# insert some data to course table

insert_course_query = """
INSERT INTO test_db.Course (name, release_year, direction)
VALUES
    ("Engineering Analytics", '2000-06-21', "IT"),
    ("System Administration", '2000-07-21', "IT"), 
    ("Enterprise management", '2000-08-21', "Management")
"""
insert_data(insert_course_query)

# insert some data to student table
insert_student_query = """
INSERT INTO test_db.Student (first_name, last_name, date_of_birth, course_id)
VALUES
    ("Tom", "Hold", "2000-09-21", 1),
    ("Eva", "Klark", "2000-07-21", 2), 
    ("Rob", "Gred", "2000-08-21", 3),
    ("Bob", "Palm", "2000-06-21", 2)
"""
insert_data(insert_student_query)

# fetch the data
print("Fetching the courses")
fetch_query = "SELECT * FROM test_db.Course"
print(fetch_data(fetch_query))

print("Fetching the courses")
fetch_query = "SELECT * FROM test_db.Student"
print(fetch_data(fetch_query))


# close the connection
cursor.close()
connection.close()