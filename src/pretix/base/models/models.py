from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)  # ID pesanan unik dari Midtrans
    status = models.CharField(max_length=50)  # Status transaksi: Pending, Success, Failed, dll.
    payment_type = models.CharField(max_length=50, blank=True, null=True)  # Tipe pembayaran (ex: credit_card, gopay)
    transaction_time = models.DateTimeField(blank=True, null=True)  # Waktu transaksi
    settlement_time = models.DateTimeField(blank=True, null=True)  # Waktu penyelesaian transaksi
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Total transaksi

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
