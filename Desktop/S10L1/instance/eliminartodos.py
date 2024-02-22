from app import create_app, db
from app.models import Data

# Crea una instancia de la aplicación Flask
app = create_app('development')

# Función para borrar todos los datos de la tabla si existen
def delete_existing_data():
    with app.app_context():
        # Verifica si la tabla existe en la base de datos
        if db.engine.has_table(Data.__tablename__):
            # Elimina todos los datos de la tabla
            Data.query.delete()
            # Guarda los cambios en la base de datos
            db.session.commit()
            print("Se han eliminado todos los datos existentes en la tabla.")
        else:
            print("La tabla no existe en la base de datos. No se realizó ninguna operación.")


if __name__ == "__main__":
    # Llama a la función para borrar los datos existentes
    delete_existing_data()
