from django.db import models
from django.contrib.auth.models import User
from datetime import date

CATEGORY_CHOICES = [
    ("food", "Food"),
    ("transport", "Transport"),
    ("shopping", "Shopping"),
    ("bills", "Bills"),
    ("other", "Other"),
]

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.category} - {self.amount}"