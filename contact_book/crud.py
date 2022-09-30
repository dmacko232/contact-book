import sqlite3
from typing import List

from contact_book.model import Contact, CreateContact


def create_contact(conn: sqlite3.Connection, contact: CreateContact) -> None:
    
    with conn:
        conn.execute(
            "INSERT INTO contacts (name, address, phone, email) VALUES(?, ?, ?, ?);",
            (contact.name, contact.address, contact.phone_number, contact.email)
            )


def read_contacts(conn: sqlite3.Connection) -> List[Contact]:
    
    res = conn.execute("SELECT * FROM contacts;")
    return [Contact(*t) for t in res.fetchall()]


def update_contact(conn: sqlite3.Connection, contact: Contact) -> None:
    
    with conn:
        conn.execute(
            """
            UPDATE contacts SET 
            name=?, address=?, phone=?, email=?,
            WHERE id=?;
            """,
            (contact.name, contact.address, 
            contact.phone_number, contact.email, 
            contact.id)
        )


def delete_contact(conn: sqlite3.Connection, id: int) -> None:
    
    with conn:
        conn.execute("DELETE FROM contacts WHERE id=?;", (id,))