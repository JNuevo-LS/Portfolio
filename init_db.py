import sqlite3 as sql

connection = sql.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Weather App', 'Deploying OpenWeatherMap API to gather data in json format and using PyQt6 module to create an user interface, shows weather for current day and forecast for the next 5 days and built-in ability to refresh data. Written in Python.',
              '10/17/2023', 'https://github.com/JNuevo-LS/Projects/blob/main/weather.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('To-Do-List', 'Devised interactive to-do list application  controlling Tkinter GUI module. Includes key bindings to add and remove from listbox along with code to save list through multiple uses employing OS module. Written in Python.', '09/27/2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/to-do-list.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Base Jumper', 'Converts between any base from binary (Base 2) to hexadecimal (Base 16). Utilizes multiple functions and accurately tested. Written in Python.', '09/24/2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/Base%20Jumper.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Cryptography', 'Developed Caesar and Vigenere cryptography methods of encoding and decoding messages for safety. Incorporates ability to brute-force Caesar-coded messages. Written in Python.', '09/21/2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/Cryptography%20COMBINED')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Magic 8-Ball', 'Composed to include user inputs, output delay + “Thinking…” status, and ability to loop program endlessly. Questions facilitated by random number generation and selection. Made to understand between different responses to continue questions or not. Written in Python.', 'Sept. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/magic%208%20ball.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Bandwidth Monitor', 'Constructed script to return bandwidth sent, received, and total in last second as well as simultaneously converting Bytes to MB for effortless reading. Written in Python.', 'Sept. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/Bandwidth%20monitor')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Coin Estimator by Weight', 'Using the weight of different stacks of coins, estimates how many coins are in the stack. Written in Python.', 'Sept. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/coin%20estimator%20by%20weight.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Fibonacci List', 'Calculates and then returns given nth digit of the fibonacci sequence. Written in Python.', 'Sept. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/fibonacci.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Change Calculator', 'Using given specific cost and payment, returns how many coins and how many of each type need to be returned to a hypothetical buyer. Written in Python.', 'Sept. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/change%20calculator.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('99-Bottles', 'Automated creation of 99-Bottles lyrics with string manipulation and iteration counting. Written in Python.', 'Aug. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/99%20bottles.py')
            )

cur.execute("INSERT INTO projects (title, content, date_created, github_link) VALUES (?, ?, ?, ?)",
            ('Countdown Timer', 'Using Time and Datetime Python modules, created countdown timer until desired time. Written in Python.', 'Aug. 2023',
             'https://github.com/JNuevo-LS/Projects/blob/main/countdown.py')
            )


connection.commit()
connection.close()