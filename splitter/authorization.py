from tastypie.authorization import Authorization
from django.db.models import Q
from splitter.models import Group, Group_Friend, Expense, Expense_Total, Settle
from django.db.models.query import QuerySet
import pickle
from itertools import chain

class Group_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(creater=bundle.request.user) | Q(group_friends__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(creater=bundle.request.user) | Q(group_friends__id=bundle.request.user.id)):
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(creater=bundle.request.user) | Q(group_friends__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(creater=bundle.request.user) | Q(group_friends__id=bundle.request.user.id)):
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(creater=bundle.request.user) | Q(group_friends__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(creater=bundle.request.user) | Q(group_friends__id=bundle.request.user.id)):
            return True
        else:
            return False
    #pass

class Group_Friend_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id)):
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id)):
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(friend__id=bundle.request.user.id)):
            return True
        else:
            return False
    #pass



class Expense_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__id=bundle.request.user.id)):
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__id=bundle.request.user.id)):
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(group__creater__id=bundle.request.user.id) | Q(payer__id=bundle.request.user.id) | Q(splitters__id=bundle.request.user.id)):
            return True
        else:
            return False
    #pass


class Expense_Total_Authorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()

    def read_detail(self, object_list, bundle):
        if object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)):
            return True
        else:
            return False

    def update_list(self, object_list, bundle):
        return object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()

    def update_detail(self, object_list, bundle):
        if object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)):
            return True
        else:
            return False

    def delete_list(self, object_list, bundle):
        return object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()

    def delete_detail(self, object_list, bundle):
        if object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)):
            return True
        else:
            return False
    #pass


class Settle_Authorization(Authorization):
    # def read_list(self, object_list, bundle):
    #     return object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()
    #
    # def read_detail(self, object_list, bundle):
    #     if object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)):
    #         return True
    #     else:
    #         return False
    #
    # def update_list(self, object_list, bundle):
    #     return object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()
    #
    # def update_detail(self, object_list, bundle):
    #     if object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)):
    #         return True
    #     else:
    #         return False
    #
    # def delete_list(self, object_list, bundle):
    #     return object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)).distinct()
    #
    # def delete_detail(self, object_list, bundle):
    #     if object_list.filter(Q(sender__id=bundle.request.user.id) | Q(receiver__id=bundle.request.user.id)):
    #         return True
    #     else:
    #         return False
    pass
