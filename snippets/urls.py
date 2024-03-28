from django.urls import path
from snippets import views

urlpatterns = [
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path('register-user/', views.RegisterUser.as_view()),
    path('api-auth/logout/', views.APILogoutView.as_view(), name='api_logout'),
    
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
    
]
