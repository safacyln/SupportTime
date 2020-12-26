from django.contrib import admin
from .models import Customers
# Register your models here.


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):

      list_display = ["customer_Name", "customer_Email", "customer_Phone", "starting_date", "due_date"]

      list_display_links = ["customer_Name", "customer_Email", "customer_Phone", "starting_date", "due_date"]

      search_fields = ["customer_Name"]

      list_filter = ["starting_date", "due_date"]

      class Meta:
        model = Customers