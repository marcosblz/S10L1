Guía de Onboarding para el Repositorio del Proyecto S10L1

¡Bienvenido al equipo! A continuación, te explicamos cómo configurar tu entorno local y comenzar a contribuir:

1. Clonar el Repositorio:

Clona el repositorio de GitHub a tu máquina local utilizando el siguiente comando en la terminal:

git clone https://github.com/marcosblz/S10L1

2. Instalar Dependencias y Configurar la Base de Datos:

Ejecuta el archivo instalarreqs-creardb.sh para instalar las dependencias y crear la base de datos local utilizando el siguiente comando en la terminal:

bash instalarreqs-creardb.sh

3. Añadir o Eliminar Datos en la Base de Datos:

Para añadir o eliminar todos los datos de la base de datos local, puedes utilizar los siguientes scripts ubicados en la carpeta instance:
añadirdatos.py: Agrega datos a la base de datos.
eliminartodos.py: Elimina todos los datos de la base de datos.

4. Ejecutar Pruebas Locales:

Para ejecutar las pruebas locales y asegurarte de que todo funciona como se espera, utiliza el siguiente comando en la terminal:

pytest

Para conocer la cobertura de tus pruebas puedes usar el siguiente comando en la terminal:

coverage run -m pytest tests
coverage report

5. Contribuir al Proyecto:

Ahora que está todo configurado en tu entorno local, puedes comenzar a contribuir al proyecto. Asegúrate de seguir las normas de colaboración definidas en el archivo CONTRIBUTING.md, incluyendo el flujo de trabajo con Git y cualquier otra directriz específica del proyecto.

6. Documentación Adicional:

Para obtener más información sobre la arquitectura del software, cómo ejecutar los tests, y otros aspectos del proyecto, consulta los archivos ARCHITECTURE.md, TESTS.md, y cualquier otro archivo relevante en la raíz del repositorio.