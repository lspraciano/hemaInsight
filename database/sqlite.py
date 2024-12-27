import sqlite3

sqlite_connection: sqlite3.Connection = sqlite3.connect(
    database="checkpoint.db",
    check_same_thread=False
)
