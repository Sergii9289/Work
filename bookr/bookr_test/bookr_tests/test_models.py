from ..models import Publisher
from django.test import TestCase


class TestPublisherModel(TestCase):
    def setUp(self):  # Model object is created every time a new test method is executed inside this test case
        self.p = Publisher(
            name='Packt',
            website='www.packt.com',
            email='contact@packt.com')

    def test_create_publisher(self):  # validates whether object was created successfully or not
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):  # whether the generated string representation of the model
        self.assertEquals(str(self.p), 'Packt')  # matches the one we are expecting
