from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.template.response import TemplateResponse


class BookrAdmin(admin.AdminSite):
    site_header = 'Bookr Administration Portal'  # змінюємо заголовок сторінки адмін
    site_title = "Bookr Administration Portal"
    index_title = "Bookr Administration"
    logout_template = 'admin/logout.html'  # перенаправляємо на новий наш шаблон
    # D:\Python\PyProjects\bookr\templates\admin\logout.html

    def profile_view(self, request):
        request.current_app = self.name  # використовується для вказівки, який додаток обробляє поточний запит
        context = self.each_context(request)
        # використовується для додавання контексту, який є спільним для всіх шаблонів адміністративного інтерфейсу
        context['username'] = request.user.username  # adding variables to context
        return TemplateResponse(request, 'admin/admin_profile.html', context)

    def get_urls(self):  # overrides the AdminSite.get_urls() method and returns the mapping of your new view
        urls = super().get_urls()  # method returns the urlpatterns list that maps to the AdminSite views.
        url_patterns = [
            path('admin_profile', self.admin_view(self.profile_view))
            ]  # wrapped your profile_view method inside the admin_view() method
        # функція гарантує, що жжоден користувач без прав адміністратора не має доступу
        return url_patterns + urls
