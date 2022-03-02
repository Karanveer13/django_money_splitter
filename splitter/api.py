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
            "username":('exact', 'startswith')
        }

# class Group_Resource(ModelResource):
#     creator = fields.ForeignKey(User_Resource, attribute = 'creator', null = True, full = True)
#     friends = fields.ToManyField(User_Resource, attribute = 'friends', null = True, full = True)
#
#     class Meta:
#         queryset = Group.objects.all()
#         resource_name = 'group'
#         authentication = ApiKeyAuthentication()
#         #authorization = Group_Authorization()
#         #always_return_data = True
#         filtering = {
#             'creator': ALL_WITH_RELATIONS,
#             'friends': ALL_WITH_RELATIONS,
#         }
    # def obj_create(self, bundle, **kwargs):
    #     bundle = self.full_hydrate(bundle)
    #     return super(Group_Resource, self).obj_create(bundle, creator=bundle.request.user)
            #pass
    # class Meta:
    #     queryset = Group.object.all()
    #     resource_name = 'group'
        #pass


# class Friend_Resource(ModelResource):
#     group = fields.ForeignKey(Group_Resource, attribute='group', null=True, full=True)
#     friend = fields.ToManyField(User_Resource, attribute='friend', null=True, full=True)
#
#     class Meta:
#         queryset = Friend.objects.all()
#         resource_name = 'friend'
#         allowed_methods = ['get']
#         authentication = ApiKeyAuthentication()
#         authorization = Friend_Authorization()
#     #pass
#
#
# class Expense_Resource(ModelResource):
#     pass
#
#
# class Expense_Total_Resource(ModelResource):
#     pass


# class Debt_Resource(ModelResource):
#     pass