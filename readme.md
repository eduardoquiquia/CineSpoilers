# 🎬 Cinespoilers API
## **Integrantes**
- Eduardo Quiquia

## 📖 Descripción general
**Cinespoilers API** es una solución backend enfocada en la administración de películas dentro de un sistema de cine.

Permite registrar, consultar, actualizar y eliminar películas mediante endpoints REST. También permite registrar géneros cinematográficos como acción, drama, terror o comedia, y asociarlos a una o varias películas.

El proyecto utiliza **Django REST Framework**, lo que facilita la creación de una API limpia, ordenada y fácil de probar desde el navegador.

## 🎯 Objetivos del proyecto

Los principales objetivos de este proyecto son:

- Desarrollar una API REST funcional usando Django y Django REST Framework.
- Aplicar operaciones CRUD sobre películas.
- Crear una entidad `Genre` para administrar géneros.
- Relacionar `Movie` y `Genre` mediante una relación muchos a muchos.
- Utilizar serializers para transformar datos entre objetos Python y JSON.
- Gestionar datos desde el panel administrativo de Django.
- Probar los endpoints desde la Browsable API.
- Mantener una base simple y ordenada para futuras mejoras.

## ⚙️ Funcionalidades principales
Actualmente, el sistema permite:

- CRUD de movies
- CRUD de genres

## 🚀 Tecnologías utilizadas
Este proyecto fue desarrollado con las siguientes tecnologías:

- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub

## **🖼️ Evidencias** 
## 1. Listar peliculas (GET)
**Ruta:** `GET /api/movies/`
![GET movie](docs/eduardo/image.png)

## 2. Crear pelicula (POST)
**Ruta:** `POST /api/movies/`
![POST movie](docs/eduardo/moviegk.png)

## 3. Actualizar pelicula (PUT)
**Ruta:** `PUT /api/movies/4`
![PUT movie](docs/eduardo/updategk.png)

## 4. Eliminar pelicula (DELETE)
**Ruta:** `DELETE /api/movies/4`
![DELETE movie](docs/eduardo/deletegk.png)

## 5. Data Base - Movies
![TABLA MOVIES](docs/eduardo/db_movies.png)

## 6. Listar genres
**Ruta:** `GET /api/genres/`
![GET genres](docs/eduardo/genres.png)
--
## 7. Crear genres
**Ruta:** `POST /api/genres/`
![POST genres](docs/eduardo/genre1.png)
![POST genres](docs/eduardo/genre2.png)

## 8. Actualizar genre
**Ruta:** `PUT /api/genres/1`
![PUT genre](docs/eduardo/genret.png)

## 9. Eliminar genre
**Ruta:** `DELETE /api/genres/1`
![DELETE movie](docs/eduardo/genredelete.png)

## 10. Data Base - Genres
![TABLA GENRES](docs/eduardo/db_genres.png)
