# 0x0F. Python - Object-relational mapping
`Python` `OOP` `SQL` `MySQL` `ORM` `SQLAlchemy`

## Before you start…
Please make sure your MySQL server is in 8.0 -> [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.alxswe.com/projects/272)

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```mysql
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
   print(row)
cur.close()
conn.close()
```

With an ORM:
``` sql
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
	Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
  print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Resources
Read or watch:

- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation-please don’t pay attention to _mysql](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial()](https://www.mikusa.com/python-mysql-docs/index.html) 
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements

* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Files will be executed with MySQLdb version 2.0.x
* Files will be executed with SQLAlchemy version 1.4.x
* All files should end with a new line
* The first line of all files should be exactly #!/usr/bin/python3
* A **README.md** file, at the root of the folder of the project, is mandatory
* Code should use the pycodestyle (version 2.8.*)
* All files must be executable
* The length of files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* You are not allowed to use execute with sqlalchemy

# More Info 
This guide outlines how to install MySQLdb module version 2.0.x on an Ubuntu 20.04 system. 

## Prerequisites
* MySQL 8.0 installed on Ubuntu 20.04 system

## Installation 
1. Install the Python development headers:
   ```
   $ sudo apt-get install python3-dev
   ```
2. Install the MySQL client development headers:
   ```
   $ sudo apt-get install libmysqlclient-dev
   ```
3. Install the Zlib development headers:
   ```
   $ sudo apt-get install zlib1g-dev
   ```
4. Install the MySQLdb module using pip3:
   ```
   $ sudo pip3 install mysqlclient
   ```
5. Confirm the installation of MySQLdb module:
   ```
   $ python3
   >>> import MySQLdb
   >>> MySQLdb.version_info
   (2, 0, 3, 'final', 0)
   ```
# Install SQLAlchemy Module

To install SQLAlchemy module version 1.4.x, follow the instructions below:

```
$ sudo pip3 install SQLAlchemy
```

You can check if the installation was successful by running the following code in Python:

```
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

Note: You may encounter the following warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)
```
