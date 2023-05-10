from django.contrib import admin

# Register your models here.
from  .models import Destination
from .models import Person
admin.site.register(Destination)
admin.site.register(Person)

