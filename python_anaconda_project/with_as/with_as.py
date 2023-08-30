import datetime
import time

"""
The with statement in Python is used to create a context for a block of code
that should be executed with some special context or setup.
"""

class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return "Hello, context!"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContextManager() as context_variable:
    print(context_variable)

"""
# Using 'with' to automatically close the file when done
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed when exiting the block
"""

class Timer:
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.datetime.now()
        print(f"Elapsed time: {self.end_time - self.start_time} seconds")

with Timer() as timer:
    time.sleep(2)
# Elapsed time: 2.00014591217041 seconds


"""
import sqlite3

class Database:
    def __enter__(self):
        self.connection = sqlite3.connect('mydb.db')
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

with Database() as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mytable")
"""

class CustomException(Exception):
    pass

class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == CustomException:
            print("CustomException handled.")
            return True  # Suppress the exception
        return False

with MyContext() as context:
    raise CustomException("This is a custom exception.")

