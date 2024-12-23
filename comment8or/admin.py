from django.contrib import admin

class Comment8orAdminSite(admin.AdminSite):
    site_title = 'Comment8or Admin'
    site_header = 'Comment8or Administration'
    index_title = 'Comment8or site admin'
    logout_template = 'logged_out.html'
