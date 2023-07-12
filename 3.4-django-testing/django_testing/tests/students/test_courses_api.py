import json

import pytest
from rest_framework.test import APIClient
from students.models import Student, Course
from model_bakery import baker
from django.urls import reverse


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def student(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return student


@pytest.mark.django_db
def test_courses_api(client):
    Student.objects.create(name='Иван')
    Course.objects.create(name='Нетология')
    response = client.get('/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == 'Нетология'


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    the_course = course_factory(_quantity=1)
    its_id = the_course[0].id
    url = reverse("courses-list")
    response = client.get(url + f'{its_id}/')
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json.get('id') == its_id


@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse("courses-list")
    courses_id = courses[1].id
    response = client.get(url, data={'id': courses_id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses_id


@pytest.mark.django_db
def test_filter_name_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse("courses-list")
    courses_name = courses[1].name
    response = client.get(url, data={'name': courses_name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses_name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    res = client.post('/courses/', data={'name': 'Нетология'})
    assert res.status_code == 201
    response = client.get('/courses/')
    data = response.json()
    assert count + 1 == Course.objects.count()
    assert data[0]['name'] == 'Нетология'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    course_id = course.id
    url_u = reverse("courses-detail", args=[course_id, ])
    data = json.dumps({'name': 'Python'})
    res = client.patch(url_u, data=data, content_type='application/json')
    assert res.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    course_id = course.id
    url_u = reverse("courses-detail", args=[course_id, ])
    data = json.dumps({'name': 'Python'})
    res = client.delete(url_u, data=data)
    assert res.status_code == 204
