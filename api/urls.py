from django.urls import path
from .views import *

urlpatterns = [
    path('mastercategory/',MasterCategoryListCreateView.as_view(),name="master-category"),
    path('mastercategory/<pk>/',MasterCategoryRetrieveUpdateDestroyView.as_view(),name="master-category-update"),
    path('masterservice/<pk>/',MasterServiceRetrieveUpdateDestroyView.as_view(),name="master-service-update"),
    path('masterservice/',MasterServiceListCreateView.as_view(),name="master-service"),
]