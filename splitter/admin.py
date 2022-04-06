from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Profile_Friend, Group, Group_Friend, Expense, Splitters, Expense_Total, Settle
# Register your models here.

#admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Profile_Friend)
admin.site.register(Group)
admin.site.register(Group_Friend)
admin.site.register(Expense)
admin.site.register(Splitters)
admin.site.register(Expense_Total)
admin.site.register(Settle)