from django.contrib import admin

# Register your models here.
from .models import State
from .models import District

admin.site.register(State)
admin.site.register(District)
