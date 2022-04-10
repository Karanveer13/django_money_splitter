# import time
# import json
#
# from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder
# #from rest_framework.serializers import ModelSerializer
# from tastypie.serializers import Serializer
# from tastypie.serializers import Serializer
# from .models import Expense, Expense_Splitter
#
# class Expense_Splitter_Serializer(Serializer):
#
#     expense = serializers.Field(source='expense.id')
#     e_expense = serializers.Field(source='e_expense.id')
#
#     class Meta:
#         model = Expense_Splitter
#
#         fields = ('expense', 'e_splitter', 'owes', )
#
#
#
# class Expense_Serializer(Serializer):
#     splitters = Expense_Splitter_Serializer(source='expense_splitter_set', many=True)
#
#     class Meta:
#         model = Expense
#
#
#
#
#
# # class MemberSerializer(ModelSerializer):
# #     groups = MembershipSerializer(source='membership_set', many=True)
# #
# #     class Meta:
# #         model = Member
# #
# # class GroupSerializer(ModelSerializer):
# #     class Meta:
# #         model = Group