from django.test import TestCase, RequestFactory
from ..views import index


class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('')  # створюємо request для URL
        request.session = {}  # обнуляємо сесію
        response = index(request)  # виклик view зі зміненим request
        self.assertEquals(response.status_code, 200)