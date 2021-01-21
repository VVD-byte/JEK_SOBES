from django.contrib import admin
from .models import User, Session, Action

admin.site.register(User)
admin.site.register(Session)
admin.site.register(Action)