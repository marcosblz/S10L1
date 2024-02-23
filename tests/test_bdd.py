import pytest
from app.models import Data
from app import create_app, db



# Fixture para configurar la aplicación antes de ejecutar las pruebas
@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()  # Crear todas las tablas en la base de datos
        yield app  # Proporcionar la aplicación para las pruebas
        db.session.remove()
        db.drop_all()  # Eliminar todas las tablas después de las pruebas

# Prueba de conexión a las rutas (endpoints)
def test_routes(app):
    client = app.test_client()  # Crear un cliente de prueba

    # Prueba de la ruta de inicio
    response = client.get('/')
    assert response.status_code == 404

    # Prueba de la ruta de inserción de datos
    response = client.post('/data', json={"name": "Test Data"})
    assert response.status_code == 200
    assert b'Data inserted successfully' in response.data

    # Prueba de la ruta de obtención de todos los datos
    response = client.get('/data')
    assert response.status_code == 200
    assert b'Test Data' in response.data

# Prueba de interacción con la base de datos
def test_database_interaction(app):
    # Insertar un nuevo dato en la base de datos
    new_data = Data(name="Test Data")
    db.session.add(new_data)
    db.session.commit()

    # Verificar que el dato se haya guardado correctamente en la base de datos
    assert Data.query.filter_by(name="Test Data").first() is not None

    # Eliminar el dato de la base de datos
    Data.query.filter_by(name="Test Data").delete()
    db.session.commit()

    # Verificar que el dato se haya eliminado correctamente de la base de datos
    assert Data.query.filter_by(name="Test Data").first() is None