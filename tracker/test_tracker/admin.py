from django.contrib import admin
from .models import Test, Club, Specialist, TestType, Specialist, Component, Variable, Winner, Status
# Register your models here.
admin.site.register(Test)
admin.site.register(Club)
admin.site.register(Specialist)
admin.site.register(TestType)
admin.site.register(Component)
admin.site.register(Variable)
admin.site.register(Winner)
admin.site.register(Status)