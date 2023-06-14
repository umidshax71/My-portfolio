from django.contrib import admin

# Register your models here.
from .models import Portfolio
admin.site.register(Portfolio),
from.models import Statistics
admin.site.register(Statistics),
from.models import Skills
admin.site.register(Skills),
from.models import Services
admin.site.register(Services),
from.models import Contact
admin.site.register(Contact)

