import sys

from contact_book.database import create_database_connection
from contact_book.utils import (
    handle_command, read_command
    )


def main() -> None:
    
    conn = create_database_connection("./db/contacts.sqlite")
    if conn is None:
        print("Exiting because connection couldn't be established.")
        sys.exit(-1)

    while True:
        command = read_command()
        handle_command(conn, command)
    

if __name__ == "__main__":
    main()
