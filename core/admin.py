from django.contrib import admin

# Register your models here.
from core.models import Location, Person, Epidemic

admin.site.register(Location)
admin.site.register(Person)
admin.site.register(Epidemic)
