"""money_splitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from tastypie.api import Api
from splitter.api import User_Resource
from splitter.api import User_Resource
#from splitter.api import User_Resource, Group_Resource, Friend_Resource, Expense_Resource, Expense_Total_Resource
from splitter.authentication import New_Resource
from . import views

# v1_api = Api(api_name = 'v1')
# v1_api.register(Splitter_Resource())
# v1_api.register(User_Resource())
# v1_api.register(Group_Resource())
# v1_api.register(Friend_Resource())
# v1_api.register(Expense_Resource())
# v1_api.register(Expense_Total_Resource())

new_resource = New_Resource()
user_resource = User_Resource()
# group_resource = Group_Resource()
# friend_resource = Friend_Resource()
# expense_resource = Expense_Resource()
# expense_total_resource = Expense_Total_Resource()
#debt_resource = Debt_Resource()

urlpatterns = [
    #re_path(r'^api/', include(v1_api.urls))
    #path('', views.home, name="home"),
    # path('signup', views.signup, name="signup"),
    # path('signin', views.signin, name="login"),
    # path('signout', views.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('', include(new_resource.urls)),
    path('', include(user_resource.urls)),
    # path('', include(group_resource.urls)),
    # path('', include(friend_resource.urls)),
    # path('', include(expense_resource.urls)),
    # path('', include(expense_total_resource.urls)),
    #path('', include(debt_resource.urls)),
]






# from django.contrib import admin
# from django.urls import path,include
# #from splitter.views import home, signup, signin, signout, activate
# from . import views
#
# urlpatterns = [
#     path('', views.home, name="home"),
#     path('signup', views.signup, name="signup"),
#     path('signin', views.signin, name="login"),
#     path('signout', views.signout, name="signout"),
#     path('activate/<uidb64>/<token>', views.activate, name="activate"),
#     #path('', home, name="home"),
#     #path('signup', signup, name="signup"),
#     #path('signin', signin, name="signin"),
#     #path('signout', signout, name="signout"),
#     #path('activate/<uidb64>/<token>', activate, name="activate"),
# ]