from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/add/', add_order, name='add_order'),
    path('accounts/profile/add/done/', AddOrderDoneView.as_view(), name='add_order_done'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/delete/<int:pk>/', delete_order, name='delete_order'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('team/', all_team, name='team'),
]
