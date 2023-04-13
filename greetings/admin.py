from django.contrib import admin
from .models import Greeting


@admin.register(Greeting)
class AddressAdmin(admin.ModelAdmin):
    pass
