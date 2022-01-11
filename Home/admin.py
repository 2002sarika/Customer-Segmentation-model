from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('Annual_Income','Spending_score','prediction')
admin.site.register(Customer)