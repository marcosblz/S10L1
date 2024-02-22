from app import create_app, db
from app.models import Data

# Crea una instancia de la aplicación Flask
app = create_app('development')


# Función para crear la tabla en la base de datos
def create_table():
    # Crea todas las tablas definidas en los modelos
    with app.app_context():
        db.create_all()


# Función para insertar datos de ejemplo en la tabla
def insert_example_data():

    create_table()
    # Inserta datos de ejemplo
    with app.app_context():
        # Datos de ejemplo
        example_data = [
            {"name": "Ejemplo 1"},
            {"name": "Ejemplo 2"},
            {"name": "Ejemplo 3"}
        ]

        # Inserta cada dato en la base de datos
        for data in example_data:
            new_data = Data(name=data["name"])
            db.session.add(new_data)

        # Guarda los cambios en la base de datos
        db.session.commit()


if __name__ == "__main__":
    # Llama a la función para insertar datos de ejemplo
    insert_example_data()
    print("Tabla creada y datos de ejemplo insertados exitosamente.")