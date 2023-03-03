"""Send an e-mail with a reminder to return the book"""
import email
from os import getenv
import sqlite3
from string import Template
from dotenv import load_dotenv
from database import Database
from borowers import get_borowers_by_return_date
from emails import Credentials, EmailSender

load_dotenv()
connection = sqlite3.connect(getenv('DB_NAME'))
ssl_enabled = getenv('SSL_ENABLED')
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')
#subject = 'Oddaj książke!'
sender = getenv('SENDER')
credentials = Credentials(username, password)


def setup(connection):
    """Create a table in the database if it doesn't exist"""
    with Database(connection) as database:
        database.cursor.execute('''CREATE TABLE borows(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        name TEXT,
        book_title TEXT,
        book_return_at DATA)''')


def send_reminder_to_borrowers(borower):
    template = Template('''Hej $name!
                    Pamiętasz, że masz moją książkę $title?? 
                    Oddaj mi ją jak najprędzej!!
                    Data zwrotu mineła $book_return_at
    ''')

    text = template.substitute({
        'name': borower.name,
        'title': borower.book_title,
        'book_return_at': borower.book_return_at
    })

    message = email.message_from_string(text)
    message.set_charset('utf-8')
    message['From'] = sender
    message['To'] = borower.email
    message['Subject'] = 'Pamiętaj o oddaniu książki!'
    connection.sendmail(sender, borower.email, message)


if __name__ == '__main__':
    borowers = get_borowers_by_return_date(connection, '2024-12-24')
    with EmailSender(port, smtp_server, credentials) as connection:
        for borower in borowers:
            send_reminder_to_borrowers(borower)
