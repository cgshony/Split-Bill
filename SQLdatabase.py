"""
This module creates the database, connects to the database,
and creates the specified tables for storing the data provided by the user.
"""

import mysql.connector

def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password"  # Replace with your actual root password
    )

    cursor = db.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS FlatmatesDB")
    cursor.execute("USE FlatmatesDB")
    cursor.close()
    db.close()

def connect_to_database():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",  # Replace with your actual root password
        database="FlatmatesDB"
    )
    return db


def create_tables():
    db = connect_to_database()
    cursor = db.cursor()

    # Create tables
    cursor.execute("CREATE TABLE IF NOT EXISTS bills (id INT AUTO_INCREMENT PRIMARY KEY, amount DECIMAL(10, 2), period VARCHAR(20))")


    cursor.execute("CREATE TABLE IF NOT EXISTS flatmates (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), days_in_house INT, bill_id INT, FOREIGN KEY (bill_id) REFERENCES bills(id))")

    # Commit changes and close connection
    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database()
    create_tables()
    print("Database   created successfully.")
