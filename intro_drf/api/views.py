from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response
from django.core.cache import cache
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

# get top sellers and top buyers data from institutions using Q
class InstitutionsView(ListAPIView):
    queryset = Institutions.objects.all()
    serializer_class = InstituionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, institution_name=None): 
        queryset = super().get_queryset()
        if institution_name:
            queryset = queryset.filter(Q(top_sellers__contains=[{'name': institution_name}]) | Q(top_buyers__contains=[{'name': institution_name}]))
        return queryset

    def list(self, request):
        institution_name = self.request.query_params.get('name', None)
        cache_key = f"institution-trade:{institution_name}"
        result = cache.get(cache_key)  
        if not result:  
            print('Hitting DB')  
            result = self.get_queryset(institution_name)  
            print(result.values())  
            
            cache.set(cache_key, result, 60)  
        else:
            print('Cache Institution Retrieved!') 
        
        result = self.serializer_class(result, many=True)
        print(result.data)  

        return Response(result.data) 
    

# get data from metadata with multiple filter using __in
class MetadataView(ListAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

    def get_queryset(self, slug_name=None):
        queryset = super().get_queryset()
        if slug_name:
            slug_name_list = slug_name.split(',')
            queryset = queryset.filter(slug__in=slug_name_list)
        return queryset

    def list(self, request):
        slug_name = self.request.query_params.get('slug', None)
        cache_key = f"metadata-trade:{slug_name}"
        result = cache.get(cache_key) 

        if not result: 
            print('Hitting DB') 
            result = self.get_queryset(slug_name)
            print(result.values())  
            
            cache.set(cache_key, result, 60)  
        else:
            print('Cache Metadata Retrieved!')  
        
        result = self.serializer_class(result, many=True)
        print(result.data)

        return Response(result.data)
    

# get sub sector name 
class SubSector(ListAPIView):
    serializer_class = SubSectorSerializer

    def get_queryset(self, sector_name=None):
        if sector_name:
            queryset = Metadata.objects.filter(sector=sector_name).values('sub_sector').distinct()
        else:
            queryset = Metadata.objects.values('sector', 'sub_sector').distinct()

        return queryset

    def list(self, request):
        sector_name = self.request.query_params.get('sector', None)
        cache_key = f"sector:{sector_name}"
        result = cache.get(cache_key) 

        if not result: 
            print('Hitting DB') 
            result = self.get_queryset(sector_name)
            print(result.values())  
            
            cache.set(cache_key, result, 60)  
        else:
            print('Cache Subsectors retrieved!')  
        
        result = self.serializer_class(result, many=True)
        print(result.data)

        return Response(result.data)
    
# get data from reportdata with multiple filter using __in
class ReportsView(ListAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

    def get_queryset(self, sub_sector_name=None):
        queryset = super().get_queryset()
        if sub_sector_name:
            sub_sector_list = sub_sector_name.split(',')
            queryset = queryset.filter(sub_sector__in=sub_sector_list)
        return queryset

    def list(self, request):
        sub_sector_name = self.request.query_params.get('sub_sector', None)
        cache_key = f"report-trade:{sub_sector_name}"
        result = cache.get(cache_key) 

        if not result: 
            print('Hitting DB') 
            result = self.get_queryset(sub_sector_name) 
            print(result.values())  
            
            cache.set(cache_key, result, 60)  
        else:
            print('Cache Reports retrieved!')  
        
        result = self.serializer_class(result, many=True)
        print(result.data)

        return Response(result.data)

# get top company by market cap
class TopReportsbyMarketCap(ListAPIView):
    serializer_class =  TopReportsbyMarketCapSerializer

    def get_queryset(self, top_n=None):
        try:
            top_n = int(top_n)
        except ValueError:
            top_n = 5
        queryset1 = Reports.objects.order_by('-total_market_cap')[:top_n]
        return queryset1
    
    def list(self, request):
        top_n = self.request.query_params.get('top', 5)
        cache_key = f"top-market-cap:{top_n}"
        result = cache.get(cache_key) 
        
        if not result: 
            print('Hitting DB') 
            result = self.get_queryset(top_n) 
            print(result.values())
            
            cache.set(cache_key, result, 60) 
        else:
            print('Cache Top Market Cap retrieved!')  
        
        result = self.serializer_class(result, many=True)
        print(result.data)
        return Response(result.data)

# get data company that have negative revenue
class NegativeRevenue(ListAPIView):
    serializer_class =  ReportsSerializer

    def get_queryset(self):
        queryset = Reports.objects.filter(avg_yoy_q_revenue_growth__lt=0)
        return queryset
    
    def list(self, request):
        cache_key = f"neg-revenue"
        result = cache.get(cache_key) 

        if not result: 
            print('Hitting DB') 
            result = self.get_queryset() 
            print(result.values())  
            
            cache.set(cache_key, result, 60)  
        else:
            print('Cache Negative Revenue Retrieved!')  
        
        result = self.serializer_class(result, many=True)
        print(result.data)

        return Response(result.data)