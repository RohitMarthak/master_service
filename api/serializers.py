from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import *


class MasterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCategory
        fields = '__all__'


class MasterServiceSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = MasterService
        fields = '__all__'

    def get_category(self, obj):
        try:
            category = obj.categories  # Assuming obj.categories is a ForeignKey to MasterCategory
            return MasterCategorySerializer(category).data
        except ObjectDoesNotExist:
            return None  # or handle the exception accordingly