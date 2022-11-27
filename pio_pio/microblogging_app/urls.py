from django.urls import path
from .views import *

app_name = "microblogging_app"

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>', PostDeleteView.as_view(),name='post-delete'),
]