from accounts.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)