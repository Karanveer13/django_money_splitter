from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key
# Create your models here.

models.signals.post_save.connect(create_api_key, sender=User)

class Profile(models.Model):
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Profile_User")
    profile_friends = models.ManyToManyField(User, through="Profile_Friend", related_name="Profile_Friends")
    def __str__(self):
        return self.profile_user.username

class Profile_Friend(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = "Profile_user")
    p_friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Profile_Friend")

    def __str__(self):
        return self.p_friend.username + ' is friend of ' + self.profile.profile_user.username

    class Meta:
        unique_together = ('profile','p_friend')

class Group(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Creator")
    name = models.CharField(max_length=250)
    group_friends = models.ManyToManyField(Profile_Friend, through="Group_Friend",  related_name="Group_Friends")
    #group_friends = models.ManyToManyField(User, through="Group_Friend", related_name="Group_Friends")
    def __str__(self):
        return self.name


class Group_Friend(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = "Group_name")
    friend = models.ForeignKey(Profile_Friend, on_delete=models.CASCADE, related_name="Profile_Friend_group")


    def __str__(self):
        return  self.friend.p_friend.username +' in group ' + self.group.name

    class Meta:
        unique_together = ('group','friend')


class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = 'Expense_group')
    amount = models.IntegerField()
    reason = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now=True)
    payer = models.ForeignKey(Group_Friend, on_delete = models.CASCADE, related_name = 'Expense_payer')
    splitters = models.ManyToManyField(Group_Friend, related_name = "Expense_splitters")
    def __str__(self):
        return self.reason + ' in group ' + self.group.name


class Expense_Total(models.Model):
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'Expense_total_sender')
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'Expense_total_receiver')
    final_amount = models.IntegerField()

    def __str__(self):
        return self.sender.username + ' gives amount ' + str(self.final_amount) + ' to ' +self.receiver.username


class Settle(models.Model):
    group = models.ForeignKey(Group,on_delete = models.CASCADE, related_name = 'Settle_group')
    expense = models.ForeignKey(Expense, on_delete = models.CASCADE, related_name = 'Settle_expense')
    sender = models.ForeignKey(Group_Friend, on_delete = models.CASCADE, related_name = 'Expense_sender')
    receiver = models.ForeignKey(Group_Friend, on_delete= models.CASCADE, related_name = 'Expense_receiver')
    amount = models.IntegerField()

    def __str__(self):
        return self.sender.friend.p_friend.username + ' has to pay ' + self.receiver.friend.p_friend.username + ' in group ' + self.group.name
































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