# Fakenews

## Alias: `Noticias Doradas`

### `Trabajo Práctico Final` - FullStack Web Development - 2022

---

### Profesor: **Gabriel Barrera**

### Alumno:

        Facundo Esteban Palermo
            Legajo: 0112674
            email: facundo.e.palermo@gmail.com
            github: facundopalermo

---
---

## Tabla de Contenido

- [Cambios respecto a la entrega del trabajo práctico en cursada](#cambios-respecto-a-la-entrega-del-trabajo-práctico-en-cursada)
- ♦ [Frameworks principales](#♦-frameworks-principales)
    - [Dependencias principales](#dependencias-principales)
        - Para Django
        - Para Vue
        - Base de datos

- ♣ [Instalación](#♣-instalación)
- ♠ [A saber](#♠-a-saber)
- ♥ [Corriendo el servidor de backend y frontend](#♥-corriendo-el-servidor-de-backend-y-frontend)
    - [El sitio](#☼-el-sitio)
    - [API REST](#api-rest)
    - [Frontend](#frontend)
        - [Implementaciones realizadas](#implementaciones-realizadas)
        - Importante
---
---
## Cambios respecto a la entrega del trabajo práctico en cursada
En la presente entrega me enfoqué sobre todo en el frontend. A continuación se detallan los cambios respecto de la entrega en cursada.

- **Backend** (Django)
    - Autor
        - Autor ahora extiende de `AbstracUser`
        - Al crear un Autor se asigna por defecto el Grupo 1 (Autor)
        - En Autor, email es el campo de inicio de sesión.
        - Al crear nuevo Autor, se valida username y email y lanza excepción si ya existen.
        - Se implementa `login/` - sesion - `logout/`.
        - Al loguear se obtienen los datos de perfil (Profile)
        - Se incororpora `profile/` con su propio serializador (no retorna la password)


- **Frontend**
    - El proyecto ahora es en base `Quasar`.
    - Se actualiza a `Pinia` en lugar de *Vuex* para la gestion de store
    - Se implementa `Axios` para las HTTP request.
    - Uso de **plugins** quasar: *Notify*
     
    - Autor:
        - Se implementa `login` y `logout` utilizando la API del backend (Mantiene sesión por medio de pinia y sessionStorage).
        - `Boton de Perfil` en el header para ver el **perfil, administrar** y **desloguear**.

    - Noticias:
        - Filtro con botones **radio** para `ordenar` en forma ascendente o descedente, y un boton para `recargar`.
        - Agregado boton (+) para `publicar noticias` con Quasar Tooltip. Requiere estar Logueado.
        - `Filtro por autor`: La página principal muestra las noticias. Cuando se imprime el *autor*, se genera la etiqueta \<a> tal que al seguir el vínculo se renderice unicamente las noticias de ese autor. **Cabe aclarar**, que para ello se hace uso del recurso *api/autores/:id/noticias/* en vez de de filtrar las ya obtenidas desde *api/noticias/*. Ello con la intención de hacer uso de la API.

    - Comentarios:
        - Agregado boton para ver comentarios, los cuales ahora se ven como ventana emergente (Quasar Dialog).
        - A continuación, si está logueado, estará habilidado el boton para agregar comentario.

    - **Administrar** es la opcion a la que se accede mediante el boton de autor. Alli se puede consultar las `noticias` y `comentarios` del autor, y `eliminar` si se desea
---
---

## ♦ Frameworks principales:

- `Django 4.0.5`
- `Quasar 2.6.0`

### Dependencias principales:

- **Para Django**:
    - Django REST Framework (3.13.1)
    - Django Cors Headers (3.13.0)
    - drf-yasg (1.20.0)
    - factory-boy (3.2.1)
    - Faker (13.13.0)

- **Para Quasar**:
    - Vue.js 3.0.0
    - Vue Router (4.0.0)
    - Pinia: (2.0.11)
    - Axios (0.27.2)

- **Base de datos**:
    - SQLite3

---
---

## ♣ Instalación

1. Tener Python 3 (+pip) y Node.js (+npm). Los siguientes pasos ejecutarlos desde este directorio.

2. Crear entorno virutual de python y activarlo (Puede variar según la terminal)

~~~
> python -m virtualenv env_django
> ./env_django/Scripts/activate
~~~

*nota: 'env_django' puede ser cualquier nombre*

3. Installar las dependencias. Para ello se incluye el archivo requirements.txt

~~~
> pip install -r requirements.txt
~~~

4. El proyecto **ya incluye una base de datos con datos ejemplo**. por lo que no es necesario hacer migrate. En caso de necesitar una base de datos nueva, se debe:

~~~
> python manage.py makemigrations
> python manage.py migrate
~~~

5. El proyecto de frontend desarrollado en **Quasar**. Para instalar las dependencias se incluyen los archivos package.json y package-lock.json. Requiere Quasar CLI

~~~
> npm -i -g @quasar/cli
~~~
~~~
> npm install
~~~

---
---

## ♠ A saber

La configuracion del backend (django -> fakenews/settings.py) es para pruebas. El Control de acceso HTTP está configurado para ello. Cualquier cosa debe configurar correctamente `CORS_ORIGIN_ALLOW_ALL` y `CORS_ORIGIN_WHITELIST`

---
---

## ♥ Corriendo el servidor de backend y frontend

1. Correr el backend (desde la raiz del proyecto)

~~~
> python manage.py runserver
~~~

2. Correr el frontend (requiere Quasar)

~~~
> npm run dev
~~~

---
---

## ☼ El sitio

1. Backend: http://localhost:8000
2. Frontend: http://localhost:9000

(configuraciones por defecto)

## ♥ Login del administrador: 

usuario: admin@localhost
pass: admin

otros usuarios:
'facundo.e.palermo@gmail.com' // 'admin'
'tininajur@gmail.com' // 'admin'
'lalolanda@email.com' // '1234'


### **API REST**:

La API REST del backend provee de los siguientes recursos
* noticias
* autores
* comentarios
* login, logout y perfil

Ademas se puede obtener:
* una noticia en particular y sus comentarios
* un autor y las noticias que hizo
* un autor y los comentarios que hizo
* un comentario en particular

Todos los detalles estan documentados y se puede acceder a ello mediante:

1. Documentación de Django REST API: http://localhost:8000/api
2. Documentación Swagger: http://localhost:8000/doc

Ademas de esos recursos, las `noticias` pueden  ser `filtradas` por `fecha`. Lamentablemente, la documentación automática no provee información respecto a los parametros que se aceptan en la URL (y no encontramos forma de hacerlo manualmente y que funcione).

Válido para:

- /noticias
- /noticias/{id}/comentarios
- /autores/{id}/noticias

Para ello se deben usar los parametros:

~~~
?fecha=dd-mm-yyyy → fecha concreta
?desde=dd-mm-yyyy → desde esa fecha
?hasta=dd-mm-yyyy → hasta esa fecha
?desde=dd-mm-yyyy&hasta=dd-mm-yyyy → entre esas fechas
~~~

### **FRONTEND**

Para el frontend se utilizó Quasar 2.6.0, vue Router v 4.0.0 y Pinia 2.0.11.

Tal como había indicado en la entrega anterior, esta vez trabajé sobre Quasar.

La decisión de usar Pinia, responde a conocer la nueva herramienta, que será la que remplace a Vuex, tal como indican los desarrolladores. Ademas Quasar también lo recomenda.

He implementado GET, POST y DELETE para los diferentes recursos.

## Implementaciones realizadas.

* Manejo de proyecto en Quasar
* Manejo de rutas en Vue Router 4
* Uso de Pinia para el store.
* Funciones varias js. Uso de Axios para las peticiones HTTP.

**IMPORTANTE**: a pesar de haber utilizado versiones mas actuales de los frameworks y librerías, se han seguido los lineamientos vistos en los videos proporcionados y los que dispone en su canal de youtube, y siguiendo la documentación oficial de cada dependencia.
