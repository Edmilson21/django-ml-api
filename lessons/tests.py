import pytest
from rest_framework.test import APIClient
from users.models import User
from lessons.models import Lesson

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def usuario_profesor():
    return User.objects.create_user(
        username='test_profesor',
        password='test1234',
        rol='profesor'
    )

@pytest.fixture
def usuario_alumno():
    return User.objects.create_user(
        username='test_alumno',
        password='test1234',
        rol='alumno'
    )

@pytest.mark.django_db
def test_alumno_puede_ver_lecciones(client, usuario_alumno):
    login = client.post('/api/users/login/', {
        'username': 'test_alumno',
        'password': 'test1234'
    })
    token = login.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.get('/api/lessons/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_alumno_no_puede_borrar_leccion(client, usuario_alumno, usuario_profesor):
    # Primero el profesor crea una lección
    leccion = Lesson.objects.create(
        titulo='Lección test',
        descripcion='Descripción test',
        creado_por=usuario_profesor
    )
    
    # El alumno intenta borrarla
    login = client.post('/api/users/login/', {
        'username': 'test_alumno',
        'password': 'test1234'
    })
    token = login.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.delete(f'/api/lessons/{leccion.id}/')
    assert response.status_code == 403

@pytest.mark.django_db
def test_profesor_puede_borrar_leccion(client, usuario_profesor):
    # El profesor crea una lección
    leccion = Lesson.objects.create(
        titulo='Lección test',
        descripcion='Descripción test',
        creado_por=usuario_profesor
    )
    
    # El profesor la borra
    login = client.post('/api/users/login/', {
        'username': 'test_profesor',
        'password': 'test1234'
    })
    token = login.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.delete(f'/api/lessons/{leccion.id}/')
    assert response.status_code == 204