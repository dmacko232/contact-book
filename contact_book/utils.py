import sqlite3

from typing import Optional, List

from contact_book.model import CreateContact, Contact
from contact_book.crud import create_contact, read_contacts, delete_contact, update_contact

CREATE_COMMAND = 0
LIST_COMMAND = 1
UPDATE_COMMAND = 2
DELETE_COMMAND = 3
INVALID_COMMAND = 4


def parse_create_contact(line: str) -> Optional[CreateContact]:
    """Parse create contact class (without id) from given line of text."""
    
    line = line.strip().split(", ")
    if len(line) != 4:
        return None
    return CreateContact(*line)


def parse_contact(line: str) -> Optional[Contact]:
    """Parse contact from given line of text."""
    
    line = line.strip().split(", ")
    if len(line) != 5:
        return None
    return Contact(*line)


def parse_id(line: str) -> Optional[int]:
    """Parse id from given line of text."""

    line = line.strip()
    try:
        return int(line)
    except ValueError as e:
        return None


def parse_command(line: str) -> int:
    """Parse command from given line of text."""

    line = line.strip().upper()
    if line == "CREATE":
        return CREATE_COMMAND
    if line == "LIST":
        return LIST_COMMAND
    if line == "UPDATE":
        return UPDATE_COMMAND
    if line == "DELETE":
        return DELETE_COMMAND
    return INVALID_COMMAND


def read_command() -> int:
    """Read command from input by user."""
    
    line = input("Please input one of the four commands below {CREATE, LIST, UPDATE, DELETE}:\n")
    command = parse_command(line)
    while command == INVALID_COMMAND:
       line = input("Only four commands {CREATE, LIST, UPDATE, DELETE} are allowed. Repeat your choice:\n")
       command = parse_command(line)
    return command


def handle_command(conn: sqlite3.Connection, command: int) -> None:
    """Handle given command by performing the IO command operation."""

    if command == CREATE_COMMAND:
        create_contact_command(conn)
    elif command == LIST_COMMAND:
        list_contacts_command(conn)
    elif command == UPDATE_COMMAND:
        update_contact_command(conn)
    elif command == DELETE_COMMAND:
        delete_contact_command(conn)


def create_contact_command(conn: sqlite3.Connection) -> None:
    """Perform the IO create contact command."""

    while True:
        line = input('Input contact data (name, address, phone_number, email) separated ", ".\n')
        contact = parse_create_contact(line)
        if contact is not None:
            create_contact(conn, contact)
            break
        else:
            print("Incorrect contact format!")


def list_contacts_command(conn: sqlite3.Connection) -> None:
    """Perform the IO list contact command."""

    contacts = read_contacts(conn)
    print_contacts(contacts)


def update_contact_command(conn: sqlite3.Connection) -> None:
    """Perform the IO update contact command."""

    ids = set(contact.id for contact in read_contacts(conn))
    while True:
        line = input('Input contact data (id, name, address, phone_number, email) separated ", ".\n')
        contact = parse_contact(line)
        if contact.id not in ids:
            print("Contact id is not present in contacts! Cant update nonexistent contact.")
            continue
        if contact is not None:
            update_contact(conn, contact)
            break
        else:
            print("Incorrect contact format!")


def delete_contact_command(conn: sqlite3.Connection) -> None:
    """Perform the IO delete contact command."""

    ids = set(contact.id for contact in read_contacts(conn))
    while True:
        line = input('Input contact id to delete:\n')
        id = parse_id(line)
        if id not in ids:
            print("Contact id is not present in contacts! Cant delete nonexistent contact.")
            continue
        delete_contact(conn, id)
        break


def print_contacts(contacts: List[Contact]) -> None:
    """Pretty print contacts."""

    print(f"id\tname\taddress\tphone\temail")
    for c in contacts:
        print(f"{c.id}\t{c.name}\t{c.address}\t{c.phone_number}\t{c.email}")

