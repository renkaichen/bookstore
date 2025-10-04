from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - ${self.total_amount}"
    
    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()  # Store price at time of order
    
    def __str__(self):
        return f"{self.book.title} x {self.quantity}"
    
    @property
    def total_price(self):
        return self.quantity * self.price
