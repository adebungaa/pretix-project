from django.contrib import admin
from .models import Order  # Import model Order dari models.py

# Daftarkan model Order di Django Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'status', 'payment_type', 'transaction_time', 'amount')
    search_fields = ('order_id', 'status')
    list_filter = ('status', 'payment_type')
