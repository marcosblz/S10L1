# Ejecución de Pruebas en el Proyecto XYZ

El proyecto S10L1 cuenta con una suite de pruebas automatizadas para garantizar la calidad del software y prevenir regresiones. A continuación se describen los pasos para ejecutar las pruebas en tu entorno local.

## Configuración del Entorno de Pruebas

1. Instala las dependencias del proyecto ejecutando el siguiente comando:
pip install -r requirements.txt

2. Configura la base de datos de pruebas ejecutando el siguiente script:
bash instalarreqs-creardb.sh

Para ejecutar las pruebas unitarias, utiliza el siguiente comando en la terminal:
pytest tests/unit

Para ejecutar las pruebas de integración, utiliza el siguiente comando en la terminal:
pytest tests/integration

El proyecto tiene como objetivo alcanzar una cobertura de pruebas del 80% o más para garantizar una adecuada protección contra regresiones. La cobertura de pruebas puede ser verificada ejecutando los siguientes comando:
coverage run -m pytest tests
coverage report