from django.contrib import admin
from .models import Accrual, Payment

admin.site.register(Accrual)
admin.site.register(Payment)
