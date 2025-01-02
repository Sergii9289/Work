from django.test import TestCase
from ..models import *
from django.contrib.auth.models import User


class TestAllModels(TestCase):
    def setUp(self):
        self.user = User(
            username='testuser', password='testpass')
        self.publisher = Publisher(
            name='Test_name',
            website='www.testname.com',
            email='testname@example.com')
        self.book = Book(
            title='Test',
            publication_date='2018-11-23',
            isbn='9781789954531',
            publisher=self.publisher)
        self.review = Review(
            content='Test Review text.',
            rating='1',
            date_created='2024-09-22 10:03:24.782232',
            date_edited='NULL',
            creator=self.user,
            book=self.book)
        self.contributor = Contributor(
            first_names='Test_Fn',
            last_names='Test_Ln',
            email='testname@example.com')
        self.bookcontributor = BookContributor(
            book=self.book,
            contributor=self.contributor,
            role='AUTHOR')

    def test_create_review(self):
        self.assertIsInstance(self.review, Review)

    def test_create_publisher(self):
        self.assertIsInstance(self.publisher, Publisher)

    def test_create_book(self):
        self.assertIsInstance(self.book, Book)

    def test_create_contributor(self):
        self.assertIsInstance(self.contributor, Contributor)

    def test_create_bookcontributor(self):
        self.assertIsInstance(self.contributor, Contributor)

    def test_str_representation_review(self):
        self.assertEquals(str(self.review), 'testuser - Test')

    def test_str_representation_publisher(self):
        self.assertEquals(str(self.publisher), 'Test_name')

    def test_str_representation_book(self):
        self.assertEquals(str(self.book), 'Test')

    def test_str_representation_contributor(self):
        self.assertEquals(str(self.contributor), 'Test_Fn Test_Ln')
