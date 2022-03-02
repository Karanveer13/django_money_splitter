from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key
# Create your models here.

models.signals.post_save.connect(create_api_key, sender=User)


class Group(models.Model):
    creater = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Creater")
    name = models.CharField(max_length=250)
    friends = models.ManyToManyField(User)
    #friends = models.ManyToManyField(User, through="Friend")
    def __str__(self):
        return self.name

class Friend(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = "Group_name")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Group_Friend")

    def __str__(self):
        return self.friend.username + ' in group ' + self.group.name

    class Meta:
        unique_together = ('group','friend')

class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = 'friend_expense')
    amount = models.IntegerField()
    reason = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now=True)
    payer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'expense_payer')
    splitters = models.ManyToManyField(User, related_name = "friends")
    def __str__(self):
        return self.reason + ' in group ' + self.group.name

class Expense_Total(models.Model):
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'expense_total_sender')
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'expense_total_receiver')
    final_amount = models.IntegerField()

    def __str__(self):
        return self.sender.username + ' gives amount ' + str(self.final_amount) + ' to ' +self.receiver.username



# class debt(models.Model):
#     group = models.ForeignKey(Group,on_delete = models.CASCADE, related_name = 'group_debts')
#     expense = models.ForeignKey(, on_delete = models.CASCADE, related_name = 'expense_debt')
#     sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'expense_sender')
#     receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'expense_receiver')
#     amount = models.IntegerField()
#
#     def __str__(self):
#         return self.sender.username + ' pay to ' + self.receiver.username + ' in room ' + self.group.name



# class room(models.Model):
#     creater = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creater")
#     name = models.CharField(max_length=250)
#     members = models.ManyToManyField(User,through="room_members")
#     #members = models.ManyToManyField(User, blank = True)
#     def __str__(self):
#         return self.name
#
# class room_members(models.Model):
#     room = models.ForeignKey(room, on_delete = models.CASCADE, related_name = "room_name")
#     #member = models.ManyToManyField(User, related_name = "room_member")
#     member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_member")
#
#     def __str__(self):
#         return self.member.username + ' in group ' + self.room.name
#
#     class Meta:
#         unique_together = ('room','member')
#
# class transaction(models.Model):
#     room = models.ForeignKey(room, on_delete = models.CASCADE, related_name = 'room_transaction')
#     amount = models.IntegerField()
#     reason = models.CharField(max_length = 250)
#     created_at = models.DateTimeField(auto_now=True)
#     payer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'transaction_payer')
#     splitters = models.ManyToManyField(User, related_name = "transaction_members")
#     def __str__(self):
#         return self.reason + ' in group ' + self.room.name
#
#
# class debt(models.Model):
#     room = models.ForeignKey(room,on_delete = models.CASCADE, related_name = 'room_debts')
#     transaction = models.ForeignKey(transaction, on_delete = models.CASCADE, related_name = 'transactions_debt')
#     sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'transaction_sender')
#     receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'transaction_receiver')
#     amount = models.IntegerField()
#
#     def __str__(self):
#         return self.sender.username + ' pay to ' + self.receiver.username + ' in room ' + self.room.name
#
# class final_transactions(models.Model):
#     sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'final_transaction_sender')
#     receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'final_transaction_receiver')
#     final_amount = models.IntegerField()
#
#     def __str__(self):
#         return self.sender.username + ' gives amount ' + str(self.final_amount) + ' to ' +self.receiver.username


































# from pyexpat import model
# from django.db import models
# from django.contrib.auth.models import User
# from django.db import models
# from tastypie.models import create_api_key
#
# models.signals.post_save.connect(create_api_key, sender=User)
#
# TASK_PRIORITY = [
#     ('Lazy', 'Lazy'),
#     ('Moderate', 'Moderate'),
#     ('Urgent', 'Urgent'),
# ]
#
# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     priority = models.CharField(max_length=12, choices=TASK_PRIORITY, default='Moderate')
#     status = models.BooleanField(default=False)
#     #tag = models.TextField()
#     #link = models.TextField()
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     assigned_to = models.ManyToManyField(User, blank=True, related_name='assigned')
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # image = models.ImageField(upload_to='image', blank=True)
#     friends = models.ManyToManyField(User, blank=True, related_name="profiles")
#     created_at = models.DateField(auto_now_add=True, null=True)
#     updated_at = models.DateField(auto_now=True)
#
#     def __str__(self):
#         return self.user.username