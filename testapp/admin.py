from django.contrib import admin
from .models import Organisation, User, Role, Member

admin.site.register(Organisation)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Member)