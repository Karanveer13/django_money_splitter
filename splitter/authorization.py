from tastypie.authorization import Authorization
from django.db.models import Q
from splitter.models import Group, Friend, Expense, Expense_Total

class Group_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(creater=bundle.request.user) | Q(friends__id=bundle.request.user.id))
    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(creater=bundle.request.user) | Q(friends__id=bundle.request.user.id)):
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(creater=bundle.request.user) | Q(friends__id=bundle.request.user.id))

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(creater=bundle.request.user) | Q(friends__id=bundle.request.user.id)):
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(creater=bundle.request.user) | Q(friends__id=bundle.request.user.id))

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(creater=bundle.request.user) | Q(friends__id=bundle.request.user.id)):
            return True
        else:
            return False
    #pass

class Friend_Authorization(Authorization):

    pass


class Expense_Authorization(Authorization):
    pass


class Expense_Total_Authorization(Authorization):
    pass


# class Debt_Authorization(Authorization):
#
#     pass

