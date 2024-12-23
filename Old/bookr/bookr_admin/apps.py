from django.contrib.admin.apps import AdminConfig


class BookrAdminConfig(AdminConfig):
    default_site = 'bookr_admin.admin.BookrAdmin'
    # вказуємо fully qualified path як шлях за замовчуванням
