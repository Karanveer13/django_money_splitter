from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie import fields
from splitter.authorization import Group_Authorization, Friend_Authorization, Expense_Authorization, Expense_Total_Authorization, Settle_Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from .models import Group, Friend, Expense, Expense_Total, Settle
from tastypie.exceptions import BadRequest
from django.db.models import Q
from django.urls import path

class User_Resource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username']
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        filtering = {
            "username":('exact', 'startswith')
        }

class Group_Resource(ModelResource):
    creater = fields.ForeignKey(User_Resource, attribute = 'creater', null = True, full = True)
    friends = fields.ToManyField(User_Resource, attribute = 'friends', null = True, full = True)

    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        allowed_methods = ['get', 'post', 'put','delete']
        authentication = ApiKeyAuthentication()
        #authorization = Authorization()
        authorization = Group_Authorization()
        always_return_data = True
        filtering = {
            'creater': ALL_WITH_RELATIONS,
            'friends': ALL_WITH_RELATIONS,
            'name': ['exact'],
        }

    def prepend_urls(self):
        return [
            path('haha/', self.wrap_view('new_me'), name="new_me"),
        ]

    def obj_create(self, bundle, **kwargs):
        bundle = self.full_hydrate(bundle)
        # return super(Group_Resource, self).obj_create(bundle, creator=bundle.request.user)
        bundle.obj = self._meta.object_class()

        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)

        bundle = self.full_hydrate(bundle)
        return self.save(bundle)

    #pass

    def obj_get(self, bundle, **kwargs):
        print(bundle)
        print(bundle.request)
        print(bundle.request.headers)
        return 123

    def new_me(self, bundle, **kwargs):
        print ("Me hu na");



class Friend_Resource(ModelResource):
    group = fields.ForeignKey(Group_Resource, attribute='group', null=True, full=True)
    friend = fields.ForeignKey(User_Resource, attribute='friend', null=True, full=True)

    class Meta:
        queryset = Friend.objects.all()
        resource_name = 'friend'
        allowed_methods = ['get', 'post', 'put','delete']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        #authorization = Friend_Authorization()
        filtering = {
            'group': ALL_WITH_RELATIONS,
            'friend': ALL_WITH_RELATIONS,
        }

        def obj_create(self, bundle, **kwargs):
            bundle = self.full_hydrate(bundle)
            return super(Friend_Resource, self).obj_create(bundle, group=bundle.request.user)
    #pass


class Expense_Resource(ModelResource):
    group = fields.ForeignKey(Group_Resource, attribute='group', null=True, full=True)
    payer = fields.ForeignKey(User_Resource, attribute='payer', null=True, full=True)
    splitters = fields.ToManyField(User_Resource, attribute='splitters', null=True, full=True)

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        allowed_methods = ['get', 'post', 'put','delete']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        #authorization = Expense_Authorization()
        filtering = {
            'group': ALL_WITH_RELATIONS,
            'payer': ALL_WITH_RELATIONS,
            'splitters': ALL_WITH_RELATIONS,
        }
    #pass


class Expense_Total_Resource(ModelResource):
    sender = fields.ForeignKey(User_Resource, attribute='sender', null=True, full=True)
    receiver = fields.ForeignKey(User_Resource, attribute='reciever', null=True, full=True)

    class Meta:
        queryset = Expense_Total.objects.all()
        resource_name = 'expense_total'
        allowed_methods = ['get', 'post', 'put','delete']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        # authorization = Expense_Total_Authorization()
        filtering = {
            'sender': ALL_WITH_RELATIONS,
            'receiver': ALL_WITH_RELATIONS,
        }
    #pass


class Settle_Resource(ModelResource):
    group = fields.ForeignKey(Group_Resource, attribute='group', null=True, full=True)
    expense = fields.ForeignKey(Expense_Resource, attribute='expense', null=True, full=True)
    sender = fields.ForeignKey(User_Resource, attribute='sender', null=True, full=True)
    receiver = fields.ForeignKey(User_Resource, attribute='receiver', null=True, full=True)
    amount = fields.IntegerField()

    class Meta:
        queryset = Settle.objects.all()
        resource_name = 'settle_payment'
        allowed_methods = ['get', 'post', 'put','delete']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        # authorization = Expense_Total_Authorization()
        filtering = {
            'group': ALL_WITH_RELATIONS,
            'expense': ALL_WITH_RELATIONS,
            'sender': ALL_WITH_RELATIONS,
            'receiver': ALL_WITH_RELATIONS,
        }
    #pass