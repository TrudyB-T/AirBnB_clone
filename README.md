# AirBnB clone - The console

## Table of contents

* [Description](#Description)
* [Command Interpreter](#Command-Interpreter)
* [Storage](#Storage)
* [Setup](#Setup)
* [Launching the Console](#Launching-the-Console)
* [Usage](#Usage)

## Description

This project is an Airbnb clone that includes a command-line console for managing various objects within the system. The console allows users to create, retrieve, update and delete objects,providing a way to interact with the Airbnb clones undderlying functionality.

## Command Interpreter

The command inbterpreter is the core component of this project. It provides a command-line interface for interacting with the Airbnb clone. Users can perform the following tasks using the console

* Create a new object of various classes.
* Retrive object from storage.
* Perform operations on objects
* Destroy/Delete an object

## Storage

The console utilizes a storage engine called __FileStorage__ to handle the storage and the retrieval of objects.

## Setup

```bash
git clone https://github.com/Dedeyd70/AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```

## Launching the Console

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit show  update

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$

* Quit command exits the console:

```bash
(hbnb) quit
$
```

## Usage
### Basic Commands and examples

> The commands are displayed in the following format *Command / usage / example with output*

* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
create <class>

```

```bash
For example:
(hbnb) create BaseModel
99894aed-5729-4436-88f6-7c764733a6eb
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
For example:
(hbnb) show BaseModel 99894aed-5729-4436-88f6-7c764733a6eb
[BaseModel] (99894aed-5729-4436-88f6-7c764733a6eb) {'id': '99894aed-5729-4436-88f6-7c764733a6eb', 'created_at': datetime.datetime(2023, 9, 14, 5, 4, 16, 989408), 'updated_at': datetime.datetime(2023, 9, 14, 5, 4, 16, 989425)}
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
For example:
(hbnb) create User
c100a9ac-3846-4459-8e47-beb4a41850a8
(hbnb) User.destroy("c100a9ac-3846-4459-8e47-beb4a41850a8")
(hbnb) User.show("c100a9ac-3846-4459-8e47-beb4a41850a8")    
** no instance found **
(hbnb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
For example:
(hbnb) create BaseModel
d8b22af2-bb5c-4ce5-a38e-60a1826302e6
(hbnb) all BaseModel
[[BaseModel] (99894aed-5729-4436-88f6-7c764733a6eb) {'id': '99894aed-5729-4436-88f6-7c764733a6eb', 'created_at': datetime.datetime(2023, 9, 14, 5, 4, 16, 989408), 'updated_at': datetime.datetime(2023, 9, 14, 5, 4, 16, 989425)}, [BaseModel] (d8b22af2-bb5c-4ce5-a38e-60a1826302e6) {'id': 'd8b22af2-bb5c-4ce5-a38e-60a1826302e6', 'created_at': datetime.datetime(2023, 9, 14, 5, 15, 52, 912755), 'updated_at': datetime.datetime(2023, 9, 14, 5, 15, 52, 912774)}]
(hbnb) 
```

* count

> *Prints the number of instances of a given class.*

```bash
For example:
(hbnb) create User
b965f795-6e0f-461c-a03e-71a3537a82f9
(hbnb) create User
55f8d113-d167-4207-9cbf-05d1d868c07e
(hbnb) User.count()
2
(hbnb)
```

* update

> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*

```bash
For example:
(hbnb) create User
debad8d8-5651-4fed-9ab7-b8c8c855c300
User.update("debad8d8-5651-4fed-9ab7-b8c8c855c300", "email", "trudo@gmail.com")  
(hbnb) User.show("debad8d8-5651-4fed-9ab7-b8c8c855c300")                               
[User] (debad8d8-5651-4fed-9ab7-b8c8c855c300) {'id': 'debad8d8-5651-4fed-9ab7-b8c8c855c300', 'created_at': datetime.datetime(2023, 9, 14, 11, 50, 53, 369243), 'updated_at': datetime.datetime(2023, 9, 14, 12, 7, 0, 630920), 'email': 'trudo@gmail'}

(hbnb)

```
