from .models import Expense
from django.contrib import admin

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "description", "date")
    search_fields = ("description",)
    list_filter = ("date",)
    
admin.site.register(Expense, ExpenseAdmin)