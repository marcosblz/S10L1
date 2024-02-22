#!/bin/bash

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Crear base de datos local
echo "Creando base de datos local..."
touch ./instance/database.db