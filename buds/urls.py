
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('bestbuy/', views.bestbuy, name='bestbuy'),
    path('topicspage/<int:id>',views.detailedview, name='detailedview'),
    path('searchpage/',views.searchpage, name='searchpage'),
    path('comparisonpage/',views.comparisonpage, name='comparisonpage'),
    path('detailedcomparisionpage/<int:id>',views.detailedcomparisionpage, name='detailedcomparisionpage'),
]
