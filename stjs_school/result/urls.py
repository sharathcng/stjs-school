from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('results/2021-2022', views.resultSearchPage, name='result-search-page'),
    path('result-view-page', views.resultView, name='resultView'),
    path('sslc-results',views.sslcResultPage, name='sslc-results'),
    path('sslc-results-statistics',views.sslcResultStats, name='sslc-results-stats'),

]