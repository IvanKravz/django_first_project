# def test_example():
#     assert False, "Just test example"
from pprint import pprint

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


@pytest.fixture
def url():
    return reverse('courses-list')

@pytest.mark.django_db
# def test_courses_api(client):
#     Student.objects.create(name='Иван')
#     Course.objects.create(name='Нетология')
#
#     response = client.get('/courses/')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 1
#     assert data[0]['name'] == 'Нетология'

# @pytest.mark.django_db
# def test_get_first_course(client, course_factory):
#     courses = course_factory(_quantity=3)


@pytest.mark.django_db
# def test_get_list_courses(client, course_factory):
#     courses = course_factory(_quantity=10)
#     response = client.get('/courses/')
#     data = response.json()
#     assert response.status_code == 200
#     assert len(data) == len(courses)
#     for i, c in enumerate(data):
#         assert c['name'] == courses[i].name


# проверка фильтрации списка курсов по id: создаем курсы через фабрику, передать
# ID одного курса в фильтр, проверить результат запроса с фильтром
# @pytest.mark.django_db
# def test_filter_list_courses(client, course_factory):
#     courses = course_factory(_quantity=10)
#     response = client.get('/courses/')
#     data = response.json()
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_create_course(client):
#     count = Course.objects.count()
#     res = client.post('/courses/', data={'name': 'Нетология'})
#     assert res.status_code == 201
#     response = client.get('/courses/')
#     data = response.json()
#     assert count + 1 == Course.objects.count()
#     assert data[0]['name'] == 'Нетология'

@pytest.mark.django_db
def test_update_course(client, course_factory, url):
    course = client.post(url, data={'name': 'Нетология'})
    assert course.status_code == 201
    course_id = course[0].id
    url_u = reverse("courses-detail", args=(str(course_id,)))
    res = client.put(url_u, data={'name': 'Python'})
    assert res.status_code == 200







    # response = client.get('/courses/')
    # data = response.json()
    # # assert count + 1 == Course.objects.count()
    # assert data[0]['name'] == 'Python'


