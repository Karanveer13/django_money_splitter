import time
import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.serializers import ModelSerializer
from tastypie.serializers import Serializer
from models import Expense, Expense_Splitter

class Expense_Serializer(ModelSerializer):
    splitters = Expense_Splitter_Serializer(source='expense_splitter_set', many=True)

    class Meta:
        model = Expense

class Expense_Splitter_Serializer(serializers.HyperlinkedModelSerializer):

    expense = serializers.Field(source='expense')
    e_splitter = serializers.Field(source='e_splitter')

    class Meta:
        model = Expense_Splitter

        fields = ('id', 'name', 'join_date', )




class MemberSerializer(ModelSerializer):
    groups = MembershipSerializer(source='membership_set', many=True)

    class Meta:
        model = Member

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group