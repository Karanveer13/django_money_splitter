from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Group, Friend, Expense,Expense_Total
# Register your models here.

#admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Friend)
admin.site.register(Expense)
admin.site.register(Expense_Total)
#admin.site.register(debt)