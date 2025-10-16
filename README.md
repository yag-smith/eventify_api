📅 Gestor de Eventos — eventify_api

API REST desarrollada con Django y Django REST Framework (DRF).
Permite administrar eventos y organizadores, donde cada evento está relacionado con un organizador.
Todo el CRUD se maneja mediante endpoints, sin usar el panel de administración de Django.

⚙️ Tecnologías utilizadas

Python 3

Django 5

Django REST Framework

SQLite (base de datos por defecto)

🚀 Instrucciones para ejecutar el servidor
# 1. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate

# 2. Instalar dependencias
pip install django djangorestframework

# 3. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 4. Ejecutar el servidor
python manage.py runserver


El proyecto se ejecutará en:
👉 http://localhost:8000/

📚 Endpoints disponibles
Método	Ruta	Descripción
GET	/api/eventos/	Listar todos los eventos
POST	/api/eventos/	Crear un nuevo evento
PUT/PATCH	/api/eventos/{id}/	Editar un evento existente
DELETE	/api/eventos/{id}/	Eliminar un evento
GET	/api/eventos/?search=	Buscar eventos por nombre o ubicación
GET	/api/organizadores/	Listar todos los organizadores
POST	/api/organizadores/	Crear un nuevo organizador
PUT/PATCH	/api/organizadores/{id}/	Editar un organizador
DELETE	/api/organizadores/{id}/	Eliminar un organizador
🧪 Ejemplos de uso con curl
# Listar eventos
curl -X GET http://localhost:8000/api/eventos/

# Crear un evento
curl -X POST http://localhost:8000/api/eventos/ \
     -H "Content-Type: application/json" \
     -d '{"nombre":"Tech Summit 2025","fecha":"2025-11-10","ubicacion":"Lima","organizador":1}'


✍️ Autor: Yair Araujo – Tecsup
📆 Ciclo IV – Diseño y Desarrollo de Software
