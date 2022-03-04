from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from django.db import IntegrityError
from tastypie.exceptions import BadRequest
from tastypie.models import ApiKey
from django.contrib.auth import authenticate, login, logout
from django.urls import path
from tastypie.http import HttpUnauthorized


class New_Resource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'new'
        excludes = ['email', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['post']
        authorization = Authorization()

    def prepend_urls(self):
        return [
            path('signup/', self.wrap_view('signup'), name="api_signup"),
            path('signin/', self.wrap_view('signin'), name="api_login"),
            path('signout/', self.wrap_view('signout'), name="api_logout")
        ]

    def signup(self, request, **kwargs):
        self.method_check(request, allowed=['get','post'])

        data = self.deserialize(request, request.body)

        username = data.get('username')
        password = data.get('password')

        if username is None:
            raise BadRequest('Enter the username')
        if password is None:
            raise BadRequest('Enter the password')

        try:
            user = User.objects.create_user(username, '', password)
            # Getting the API key
            api_key = ApiKey.objects.get(user=user.id)
            return self.create_response(request, {
                'success': True,
                'username': username,
                'token': api_key.key
            })
        except IntegrityError:
            raise BadRequest('That username already exists')

    def signin(self, request, **kwargs):
        self.method_check(request, allowed=['get','post'])
        data = self.deserialize(request, request.body)
        username = data.get('username')
        password = data.get('password')
        if username is None or password is None:
            raise BadRequest('Please enter a value.')

        # Check if the user exists
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # Getting the API key,create if doesn't exist
            try:
                api_key = ApiKey.objects.get(user=user)
                if not api_key.key:
                    api_key.save()
            except ApiKey.DoesNotExist:
                #raise BadRequest('Please enter correct details.')
                api_key = ApiKey.objects.create(user=user)

            return self.create_response(request, {
                'success': True,
                'username': username,
                'token': api_key.key
            })
        else:
            raise BadRequest("Please enter correct details.")
    def signout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.authenticated():
            logout(request)
            return self.request.create_response(request, {'success': True})
        else:
            return self.request.create_response(request, {'success': False}, HttpUnauthorized)






# class Splitter_Resource(ModelResource):
#     class Meta:
#         queryset = User.objects.all()
#         resource_name = 'splitter'
#         allowed_methods = ['post']
#         authorization = Authorization()
#         fields = ['username', 'id']
#         excludes = ['password']
#         always_return_data = True
#
#     def prepend_urls(self):
#         return [
#             path('signup/', self.wrap_view('signup'), name="api_signup"),
#             path('signin/', self.wrap_view('signin'), name="api_login"),
#             path('signout/', self.wrap_view('signout'), name="api_logout")
#         ]
#
#     def signup(self, request, **kwargs):
#         self.method_check(request, allowed=['post'])
#         data = self.deserialize(request, request.body)
#         username = data.get('username')
#         password = data.get('password')
#         if username is None or password is None:
#             raise BadRequest('Please enter a value.')
#
#         try:
#             user = User.objects.create_user(username, '', password)
#             # Getting the API key
#             api_key = ApiKey.objects.get(user=user.id)
#             return self.create_response(request, {
#                 'success': True,
#                 'username': username,
#                 'token': api_key.key
#             })
#         except IntegrityError:
#             raise BadRequest('That username already exists')
#
#     def signin(self, request, **kwargs):
#         self.method_check(request, allowed=['post'])
#         data = self.deserialize(request, request.body)
#         username = data.get('username')
#         password = data.get('password')
#         if username is None or password is None:
#             raise BadRequest('Please enter a value.')
#
#         # Check if the user exists
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             # Getting the API key,create if doesn't exist
#             try:
#                 api_key = ApiKey.objects.get(user=user)
#                 if not api_key.key:
#                     api_key.save()
#             except ApiKey.DoesNotExist:
#                 api_key = ApiKey.objects.create(user=user)
#
#             return self.create_response(request, {
#                 'success': True,
#                 'username': username,
#                 'token': api_key.key
#             })
#         else:
#             raise BadRequest("Incorrect username or password.")
#
#     def signout(self, request, **kwargs):
#         self.method_check(request, allowed=['get'])
#         if request.user and request.user.authenticated():
#             logout(request)
#             return self.request.create_response(request, {'success': True})
#         else:
#             return self.request.create_response(request, {'success': False}, HttpUnauthorized)