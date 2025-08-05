# Proyecto Django con Docker y MySQL

## Introducción

Este README proporciona una guía completa sobre cómo configurar, desarrollar y desplegar una aplicación Django utilizando Docker y Docker Compose, tanto para entornos de desarrollo como de producción.

## Prerrequisitos

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Django](https://www.djangoproject.com/)

## Entorno de Desarrollo

Para el desarrollo, puedes utilizar el archivo `docker-compose.yml` proporcionado para configurar y ejecutar tu aplicación. Esta configuración está diseñada para facilitar iteraciones rápidas y pruebas en un entorno de desarrollo.

### Pasos para Ejecutar en Modo Desarrollo

1. **Construir la Imagen**

   Primero, construye tu imagen de Docker:

   ```bash
   docker compose build
   ```

2. **Iniciar la Aplicación**

   Usa el siguiente comando para iniciar tu aplicación en modo desarrollo:

   ```bash
   docker compose up -d
   ```

   Este comando iniciará tu aplicación y sus dependencias, como la base de datos MySQL, en el entorno de desarrollo.

3. **Aplicar Migraciones**

   Una vez que los contenedores estén en funcionamiento, aplica las migraciones de la base de datos:

   ```bash
   docker compose exec web python intelligent_systems/manage.py migrate
   ```

## Ejemplo del Archivo `.env`

Asegúrate de crear un archivo `.env` en la raíz de tu proyecto con el siguiente contenido:

```env
# Variables de entorno para MySQL
DB_NAME=nombre_de_tu_base_de_datos
DB_USER=tu_usuario
DB_PASS=tu_contraseña
DB_HOST=db
DB_PORT=3306
DB_ROOT_PASS=contraseña_root

NPM_BIN_PATH='ruta node-modules'
```

# MODO DEV
## Update Dependences
pip freeze > requirements.txt

## Instalation Dependences
pip install -r requirements.txt

## Configurate .env file
.env.example

## Install Tailwind
python manage.py tailwind install

## Deploy Project
py .\manage.py tailwind start
py .\manage.py runserver

## Databases
mysql