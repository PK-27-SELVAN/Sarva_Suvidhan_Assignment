# Sarva_Suvidhan_Assignment

# Backend Assignment: API Development Task

## Assignment Title: 
**Develop any Two APIs Based on Provided Postman Collection.**

## API'S Implemented:
I chose to implement two api's,
1. **Bogie Checksheet API**
2. **Wheel Specification API**

## Tech Stack
1. **Framework** : Django,Django Rest Framework (DRF).
2. **Database** : PostgreSQL
3. **API Testing Tool** : Postman

## Key Features Implemented

- **Use of Django REST Framework's ModelViewSets**
  - Both APIs are built using `ModelViewSet`, which provides a complete set of default CRUD operations (`list`, `create`, `retrieve`, `update`, `destroy`).
  - This reduces boilerplate code and leverages DRF’s powerful routing, request parsing, and serialization features.
  - Custom `create()`,`update()` methods are overridden where needed to handle nested data serialization (e.g., Bogie and Wheel nested fields).

- **Bogie Checksheet API**
  - Implements nested serializer structure using one-to-one or foreign key relations.
  - Captures condition details of bogie components like bolster, axle guide, etc.

- **Wheel Specification API**
  - Designed using a main model (`WheelInspection`) and a nested model (`WheelFields`) to store measurements such as axle bore, roller bearing bore, etc.
  - Data is validated and saved using a custom serializer with a nested object creation strategy.

- **Postman Collection Included**
  - A ready-to-use Postman collection (`Suvi_assgn.postman_collection.json`) is provided for easy testing and validation of both APIs.


## Setting Up the Project
1. **clone the repo**
- git clone https://github.com/PK-27-SELVAN/Sarva_Suvidhan_Assignment.git

2. **create and activate the Virtual Environment**
- py -m venv env
- cd env/Scripts
- activate
- cd ../..

3. **Install Dependencies**
- pip install -r requirements.txt

4. **Apply Migarations and create a database**
- py manage.py makemigrations
- py manage.py migrate

5. **Run the developement server at localhost**
- py manage.py runserver

6. **Use Postman to test rest api**
- First,Import Suvi_assgn.postman_collection.json into Postman.
- Then test all the implemented endpoints to check for correct responses.


