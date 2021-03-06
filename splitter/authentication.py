from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from django.db import IntegrityError
from tastypie.exceptions import BadRequest
from tastypie.models import ApiKey
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from tastypie.http import HttpUnauthorized


class New_Resource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'new'
        #excludes = ['email', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['post']
        authorization = Authorization()

    def prepend_urls(self):
        return [
            # path('signup/', self.wrap_view('signup'), name="api_signup"),
            # path('signin/', self.wrap_view('signin'), name="api_login"),
            # path('signout/', self.wrap_view('signout'), name="api_logout")

            url(r'^signup/', self.wrap_view('signup'), name="api_signup"),
            url(r'^signin/', self.wrap_view('signin'), name="api_login"),
            url(r'^signout/', self.wrap_view('signout'), name="api_logout")
        ]

    def signup(self, request, **kwargs):
        self.method_check(request, allowed=['get','post'])

        data = self.deserialize(request, request.body)

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username_exist = User.objects.filter(username=username)
        print(username_exist)
        email_exist = User.objects.filter(email=email)
        if username is None:
            raise BadRequest('Enter the username')
        if password is None:
            raise BadRequest('Enter the password')
        if username_exist:
            raise BadRequest('Username already exists!!')
        if email_exist:
            raise BadRequest('Email already exists!!')

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            api_key = ApiKey.objects.get(user=user.id)
            return self.create_response(
                request, {
                    'success': True,
                    'username': username,
                    'id': user.id,
                    'first name': first_name,
                    'last name': last_name,
                    'email': email,
                    'token': api_key.key
            })
        except IntegrityError:
            raise BadRequest('Username already Exists')

    def signin(self, request, **kwargs):
        self.method_check(request, allowed=['get','post'])
        data = self.deserialize(request, request.body)
        username = data.get('username')
        password = data.get('password')

        if username is None:
            raise BadRequest('Enter the username')
        if password is None:
            raise BadRequest('Enter the password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            try:
                api_key = ApiKey.objects.get(user=user)
                if not api_key.key:
                    api_key.save()
            except ApiKey.DoesNotExist:
                api_key = ApiKey.objects.create(user=user)

            return self.create_response(
                request, {
                    'success': True,
                    'username': username,
                    'id': user.id,
                    'full_name': user.first_name + " " + user.last_name,
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
