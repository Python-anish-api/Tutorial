# from django.urls import path
# from snippets import views

# urlpatterns = [
#     path('', views.api_root),

#     path("users/", views.UserList.as_view(),name='user-list'),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name='user-list'),
#     path('register-user/', views.RegisterUser.as_view()),
#     path('api-auth/logout/', views.APILogoutView.as_view(), name='api_logout'),
    
#     path("snippets/", views.SnippetList.as_view(), name='snippet-list'),
#     path("snippets/<int:pk>/", views.SnippetDetail.as_view() ,name='snippet-detail'),
    
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]