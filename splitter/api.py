from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie import fields
from splitter.authorization import Group_Authorization, Friend_Authorization, Expense_Authorization, Expense_Total_Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from .models import Group, Friend, Expense, Expense_Total
from tastypie.exceptions import BadRequest
from django.db.models import Q

class User_Resource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username']
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "username":('exact', 'startswith');
        }

class Group_Resource(ModelResource):
    creater = fields.ForeignKey(User_Resource, attribute = 'creater', null = True, full = True)
    friends = fields.ToManyField(User_Resource, attribute = 'friends', null = True, full = True)

    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        #authorization = DjangoAuthorization()
        authorization = Group_Authorization()
        always_return_data = True
        # filtering = {
        #     'creator': ALL_WITH_RELATIONS,
        #     'friends': ALL_WITH_RELATIONS,
        # }

    # def obj_create(self, bundle, **kwargs):
    #     bundle = self.full_hydrate(bundle)
    #     return super(Group_Resource, self).obj_create(bundle, creator=bundle.request.user)
            #pass
    # class Meta:
    #     queryset = Group.object.all()
    #     resource_name = 'group'
        #pass


class Friend_Resource(ModelResource):
    group = fields.ForeignKey(Group_Resource, attribute='group', null=True, full=True)
    friend = fields.ToManyField(User_Resource, attribute='friend', null=True, full=True)

    class Meta:
        queryset = Friend.objects.all()
        resource_name = 'friend'
        allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        #authorization = Friend_Authorization()
#     #pass
#
#
class Expense_Resource(ModelResource):
    group = fields.ForeignKey(Group_Resource, attribute='group', null=True, full=True)
    payer = fields.ForeignKey(User_Resource, attribute='payer', null=True, full=True)
    splitters = fields.ToManyField(User_Resource, attribute='splitters', null=True, full=True)

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        #authorization = Expense_Authorization()
    #pass


class Expense_Total_Resource(ModelResource):
    sender = fields.ForeignKey(User_Resource, attribute='sender', null=True, full=True)
    receiver = fields.ForeignKey(User, attribute='reciever', null=True, full=True)

    class Meta:
        queryset = Expense_Total.objects.all()
        resource_name = 'expense_total'
        allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        # authorization = Expense_Total_Authorization()
    #pass


# class Debt_Resource(ModelResource):
#     pass