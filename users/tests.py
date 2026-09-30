import pytest
from rest_framework.test import APIClient
from users.models import User


""" Es simplemente una forma de no repetir APIClient() en cada test. 
Sin el fixture tendrías que escribir esto en cada función"""

@pytest.fixture
def client():  # fixture 1 — crea el cliente HTTP
    return APIClient()


""" Es una función que prepara datos que vas a necesitar en los tests. 
En vez de crear un usuario en cada test, lo creas una vez en el fixture y lo reutilizas"""
@pytest.fixture
def usuario_alumno():  # fixture 2 — crea un usuario alumno
    return User.objects.create_user(
        username='test_alumno',
        password='test1234',
        rol='alumno'
    )
    
    

""" 
Por seguridad pytest no te deja tocar la base de datos por defecto. Este decorador le dice:
"Este test sí necesita acceder a la BD, permítelo"
Sin él, cualquier test que haga una query falla automáticamente.
"""
@pytest.mark.django_db
def test_registro_usuario(client):
    response = client.post('/api/users/register/', {
        'username': 'nuevo_usuario',
        'email': 'nuevo@test.com',
        'password': 'test1234',
        'rol': 'alumno',
        'telefono': '123456789'
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_usuario(client, usuario_alumno):
    response = client.post('/api/users/login/', {
        'username': 'test_alumno',
        'password': 'test1234'
    })
    assert response.status_code == 200
    assert 'access' in response.data


@pytest.mark.django_db
def test_perfil_sin_token(client):
    response = client.get('/api/users/profile/')
    assert response.status_code == 401

@pytest.mark.django_db
def test_perfil_con_token(client, usuario_alumno):
    # Hacemos login para obtener el token
    login = client.post('/api/users/login/', {
        'username': 'test_alumno',
        'password': 'test1234'
    })
    token = login.data['access']
    
    # Usamos el token en la petición
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.get('/api/users/profile/')
    assert response.status_code == 200
    

# Tests para los permisos

@pytest.fixture
def usuario_profesor(): # fixture 3 — crea un usuario profesor
    return User.objects.create_user(
        username='test_profesor',
        password='test1234',
        rol='profesor'
    )

@pytest.mark.django_db
def test_alumno_no_puede_crear_leccion(client, usuario_alumno):
    login = client.post('/api/users/login/', {
        'username': 'test_alumno',
        'password': 'test1234'
    })
    token = login.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.post('/api/lessons/', {
        'titulo': 'Test lección',
        'descripcion': 'Test descripcion'
    })
    assert response.status_code == 403

@pytest.mark.django_db
def test_profesor_puede_crear_leccion(client, usuario_profesor):
    login = client.post('/api/users/login/', {
        'username': 'test_profesor',
        'password': 'test1234'
    })
    token = login.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.post('/api/lessons/', {
        'titulo': 'Test lección',
        'descripcion': 'Test descripcion'
    })
    assert response.status_code == 201