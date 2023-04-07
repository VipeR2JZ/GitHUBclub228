from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(CountryLanguage)
admin.site.register(Language)

