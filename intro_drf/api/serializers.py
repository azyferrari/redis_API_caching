from rest_framework import serializers
from .models import *

class InstituionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutions
        fields = '__all__'

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'

class SubSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['sector', 'sub_sector']

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class TopReportsbyMarketCapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['sub_sector', 'total_companies', 'total_market_cap']


