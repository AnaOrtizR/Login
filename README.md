# Proyecto Login

## Objetivo del proyecto:
    Generar un proyecto en python que me permita practicar mis habilidades en backend, específicamente, un módulo de login con autenticación.

## Objetivo de la applicación:
    Este módulo permitirá a los usuarios, registrarse, y acceder con su nombre de usuario y contraseña.

## Proyecto construido con: 
    Python 3.12.4
    Flask 3.0.3

## Pasos para la instalación:
    1° Clonar el proyecto en una ubicación de su comodidad.
    2° Abrir una consola (powershell o terminal del IDE).
    3° Ubicarse en la raiz del proyecto.
    4° Crear entorno virtual usando venv "python -m venv venv".
    5° Activar el entorno virtual "venv\Scripts\activate".
    6° Instalar las dependencias del archivo requirements.txt "pip install requirements.txt".
    7° Ejecutar comando "flask run" en su consola.

    Ahora estará listo para consumir la API.

## Endpoints disponibles:
### Users:
#### List Users
    Verb: GET
    Path: /users
    Respuesta esperada:
    {
        "dateCreated": "Tue, 13 Aug 2024 21:37:13 GMT",
        "dateUpdated": "Tue, 13 Aug 2024 21:37:13 GMT",
        "email": "ana@email.com",
        "fullName": "Ana Andrea Ortiz Romo",
        "id": 1,
        "passwd": "examplepass1",
        "username": "AnaOrtizR"
    }

#### Create User
    Verb: POST
    Path: /users/new
    Payload:
    {
        "fullName": "Ana Andrea Ortiz Romo"
        "username":"AnaOrtizR",
        "email":"ana@email.com",
        "passwd":"examplepass1"
    }
    Respuesta esperada:
    {
        "dateCreated": "Tue, 13 Aug 2024 21:37:13 GMT",
        "dateUpdated": "Tue, 13 Aug 2024 21:37:13 GMT",
        "email": "ana@email.com",
        "fullName": "Ana Andrea Ortiz Romo",
        "id": 1,
        "passwd": "examplepass1",
        "username": "AnaOrtizR"
    }

#### Login
    Verb: POST
    Path: /users/LoginUser
    Payload:
    {
        "username": "AnaOrtizR",
        "passwd": "examplepass1"
    }
    Respuesta esperada:
    {
    "message": "Login successful",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMzY3NzQ4OSwianRpIjoiNGI3Njg0ZjAtYjJjNy00YTM2LTkxNzMtNzQ0ZjdmMTEwMWU5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkFuYU9ydGl6UiIsIm5iZiI6MTcyMzY3NzQ4OSwiY3NyZiI6ImY3ZGYxYTk3LTNmNTUtNDcyYy1iMTcxLTBhYzgwMGQ0ZDMwZSIsImV4cCI6MTcyMzY3ODM4OX0.R5yt0WVR4jaKrtUC-ui0OA_uf6ZbpgS85j6JNt4TW5o"
    }

#### Perfil
    Verb: GET
    Path: /users/perfil
    Header:
        Authorization: Bearer token
    Respuesta esperada:
    {
    "data": {
        "Nombre": "Ana Andrea Ortiz Romo",
        "dateCreated": "Tue, 13 Aug 2024 21:37:13 GMT",
        "email": "ana@email.com",
        "username": "AnaOrtizR"
    },
    "logged_in_as": "AnaOrtizR"
}



