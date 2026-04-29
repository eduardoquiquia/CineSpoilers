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
## 1. Primera evidencia (Preparación de entorno)
![LEVANTAMIENTO](docs/levantamiento.png)

## 2. Creando movie desde Admin
![MOVIE DESDE ADMIN](docs/createmovieadmin.png)
![alt text](docs/movieadmin.png)

## 3. Obteniendo pelicula sin relacion con genres
![MOVIE SIN GENRES](docs/singenres.png)

## 4. Agregando genres a movie desde admin
![ADD GENRES A MOVIE](docs/addgenres.png)

## 5. Obteniendo pelicula con relacion de generos
![MOVIE JSON](docs/moviewithgenres.png)

## 4. Obteniendo peliculas en front
![MOVIES FRONT](docs/moviesreact.png)

## 5. Obteniendo generos en formato json
![GENRES](docs/genres.png)

## 6. Obteniendo generos en front
![GENRES FRONT](docs/genresfront.png)

## 7. Agregando app actors
![ADD ACTORS APP](docs/addactors.png)

## 8. Obteniendo actor en formato json
![GET ACTOR](docs/getactor.png)

## 8. Creando Actors desde Admin
![ADD ACTOR](docs/addactor.png)

## 9. Obteniendo actor en front
![ACTOR FRONT](docs/actorfront.png)
