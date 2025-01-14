from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    add_comment
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact-us'),
    path('home/', views.home, name='home'),
    path('district/', views.district, name='district'),
    path('regional/', views.regional, name='regional'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
]
urlpatterns += staticfiles_urlpatterns()
