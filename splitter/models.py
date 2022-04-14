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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Profile_Friend")

    def __str__(self):
        return self.user.username + ' is friend of ' + self.profile.profile_user.username

    class Meta:
        unique_together = ('profile','user')

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
        return  self.friend.user.username +' in group ' + self.group.name

    class Meta:
        unique_together = ('group','friend')


class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = 'Expense_group')
    amount = models.IntegerField()
    reason = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now=True)
    payer = models.ForeignKey(Group_Friend, on_delete = models.CASCADE, related_name = 'Expense_payer')
    settled_by = models.ManyToManyField(Group_Friend, blank=True, related_name="Expense_settled_splitters")
    splitters = models.ManyToManyField(Group_Friend, through="Expense_Splitter",related_name = "Expense_splitters")
    def __str__(self):
        return self.reason + ' in group ' + self.group.name

class Expense_Splitter(models.Model):
    expense = models.ForeignKey(Expense, on_delete = models.CASCADE, related_name = "Expense_name")
    e_splitter = models.ForeignKey(Group_Friend, on_delete=models.CASCADE, related_name="Expense_Group_Friend")
    owes = models.IntegerField()
    settle = models.BooleanField(default=False)

    # expense = models.ForeignKey(Expense, null=True, blank=True, on_delete=models.CASCADE, related_name="Expense_name")
    # e_splitter = models.ForeignKey(Group_Friend, null=True, blank=True, on_delete=models.CASCADE, related_name="Expense_Group_Friend")
    # owes = models.IntegerField(default=None)
    # settle = models.BooleanField(default=False)

    def __str__(self):
        return  self.e_splitter.friend.user.username +' in expense ' + self.expense.reason + ' owes ' + str(self.owes)

    class Meta:
        unique_together = ('expense','e_splitter')


class Expense_Total(models.Model):
    sender = models.ForeignKey(Group_Friend, on_delete = models.CASCADE, related_name = 'Expense_total_sender')
    receiver = models.ForeignKey(Group_Friend, on_delete= models.CASCADE, related_name = 'Expense_total_receiver')
    final_amount = models.IntegerField()

    def __str__(self):
        return self.sender.friend.user.username + ' gives amount ' + str(self.final_amount) + ' to ' +self.receiver.friend.user.username


class Settle(models.Model):
    group = models.ForeignKey(Group,on_delete = models.CASCADE, related_name = 'Settle_group')
    expense = models.ForeignKey(Expense, on_delete = models.CASCADE, related_name = 'Settle_expense')
    sender = models.ForeignKey(Group_Friend, on_delete = models.CASCADE, related_name = 'Expense_sender')
    receiver = models.ForeignKey(Group_Friend, on_delete= models.CASCADE, related_name = 'Expense_receiver')
    amount = models.IntegerField()
    def __str__(self):
        return self.sender.friend.user.username + ' has to pay ' + self.receiver.friend.user.username + ' in group ' + self.group.name