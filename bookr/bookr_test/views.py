from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def greeting_view_user(request):
    """Greet the user."""
    user = request.user
    return HttpResponse(f'Hey there, welcome to Bookr, {user.username}!')


