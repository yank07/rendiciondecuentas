# Plataforma de transparencia de donaciones

Este es un proyecto del [CIRD](https://cird.org.py) en colaboración con [CIVILAB](https://civilab.org.py).

Entre las funionalidades principales de la plataforma tenemos:

- Administración de donaciones recibidas
- Administración de gastos
- Listado de donaciones recibidas y compras con filtros de montos, fechas y donante.
- Detalle de compras: Items adquiridos y documentos relacionados
- Descarga en CSV y JSON de donaciones y compras

## Requerimientos

- [Python >= 3.6](https://www.python.org/)
- [Pipenv](https://github.com/pypa/pipenv)
- [PostgreSQL](https://www.postgresql.org/)
- [NodeJS](https://nodejs.org)

## Entorno de desarrollo

1. Clona este repositorio.
2. Instala las dependencias de Python: `pipenv install`.
3. Crea un archivo llamado `secrets.json` en la raíz del proyecto.
4. Inserta las siguientes líneas en el archivo:
   ```
   {
     "allowed_hosts": ["localhost", "127.0.0.1", <ANY_OTHER_HOST>],
     "db_name": "<DB_NAME>",
     "db_user": "<POSTGRESQL_DB_USER>",
     "db_password": "<POSTGRESQL_DB_PASSWORD>",
     "db_host": "<POSTGRESQL_DB_HOST>",
     "db_port": "<POSTGRESQL_DB_PORT>",
     "secret_key": "<DJANGO_SECRET_KEY>",
     "debug": "TRUE"
   }
   ```
5. Activa el entorno virtual: `pipenv shell`
6. Instala la extension `unaccent` en tu base de datos de PostgreSQL:
   ```
   $ psql -d <DB_NAME>
   <DB_NAME>=# create extension unaccent;
   ```
7. Ejecuta las migraciones: `python manage.py migrate`
8. Crea el primer superusuario: `python manage.py createsuperuser`
9. Ve a la carpeta `static_src`
10. Instala las dependencias de node `npm install`
11. Ejecuta `npm run compile:css:watch` para compilar el CSS
12. Inicia el servidor de desarrollo: `python manage.py runserver`
13. Ve a [localhost:8000/admin](localhost:8000/admin) para crear las primeras entradas.
14. Ve a [localhost:8000/](localhost:8000/) para ver el sitio web.

## Contribuye!

Puedes dejarnos bugs y sugerencias en la sección de issues [github issue tracker](http://github.com/xxx),
o mejor aún envíanos un PR con tus modificaciones.

## Licencia

Este software esta liberado bajo la licencia GPL-3.0.
