from .views import *

from django.urls import path, include

urlpatterns = [
    path('institution-trade', InstitutionsView.as_view(), name='institution-trade'),
    path('metadata-trade', MetadataView.as_view(), name='metadata-trade'),
    path('report-trade', ReportsView.as_view(), name='report-trade'),
    path('top-market-cap', TopReportsbyMarketCap.as_view(), name='top-market-cap'),
    path('neg-revenue', NegativeRevenue.as_view(), name='neg-revenue'),
    path('sub-sector', SubSector.as_view(), name='sub-sector')
    
]