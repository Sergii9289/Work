# from django.test import TestCase
# from django.contrib.auth.models import User, AnonymousUser
# from django.test import RequestFactory
# from .views import greeting_view_user
#
#
# class TestLoggedGreetingView(TestCase):
#     """Test the greeting view for the authenticated users."""
#
#     def setUp(self):
#         # Create a test user
#         self.test_user = User.objects.create_user(
#             username='testuser', password='t1e2s3t4')
#         self.test_user.save()  # This ensures that the user is saved in the database
#         # initializes a RequestFactory to create mock requests for testing views
#         self.factory = RequestFactory()
#
#     def test_greeting_not_auyhenticated(self):
#         request = self.factory.get('/test/greet_user')  # Create a GET request
#         # makes the view function think that the user making the request is not logged in
#         request.user = AnonymousUser()  # Set the user as AnonymousUser
#         response = greeting_view_user(request)  # Call the view
#         # Assert that the response status code is 302 (redirect)
#         self.assertEquals(response.status_code, 302)
#
#     def test_user_authenticated(self):
#         request = self.factory.get('/test/greet_user')
#         request.user = self.test_user
#         response = greeting_view_user(request)
#         self.assertEquals(response.status_code, 200)
