from django.urls import path

from .views import  api_view, DetailAppsView, CreateAppsView, UpdateAppsView, DeleteAppsView,AppsMixinsViews
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    #path('', api_view, name='api_view'),
    #path('<int:pk>/', DetailAppsView.as_view()),
    #path('<int:pk>/update', UpdateAppsView.as_view()),
    #path('<int:pk>/delete', DeleteAppsView.as_view()),
    path('create/', CreateAppsView.as_view()),
    #path('list/', ListAppsView.as_view()),
    path('mixins/', AppsMixinsViews.as_view()),
    path('<int:pk>/details', AppsMixinsViews.as_view(), name="apps-details"),
    path('<int:pk>/update', AppsMixinsViews.as_view()),
    path('<int:pk>/delete', AppsMixinsViews.as_view()),
    path('list/', AppsMixinsViews.as_view()),
    #path('create/', AppsMixinsViews.as_view()),
    path('auth', obtain_auth_token),
    
    
]
