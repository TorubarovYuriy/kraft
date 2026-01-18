from django.urls import path

from . import views

app_name = 'production'

urlpatterns = [
    path('', views.ProductionMainView.as_view(), name='main'),
    path('machines/', views.MachineListView.as_view(), name='machine_list'),
    path(
        'machines/<int:pk>/',
        views.MachineDetailView.as_view(),
        name='machine_detail'
    ),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path(
        'orders/<int:pk>/', views.OrderDetailView.as_view(),
        name='order_detail',
    ),
    path('clues/', views.ClueListView.as_view(), name='clue_list'),
    path(
        'clues/<int:pk>/', views.ClueDetailView.as_view(), name='clue_detail'
    ),
    path(
        'shift/', views.WorkingShiftListView.as_view(), name='working_shift'
    ),
]
