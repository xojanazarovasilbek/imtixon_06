from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:pk>', category, name='category'),
    path('category/', category_list, name='category_list'), 
    path('detail/<int:pk>', new_detail, name='detail'),
    path('create/', Post_create.as_view(), name='post_create'),
    path('profile/', profile, name='profile'),
    path('user/', user, name='user'),
    path('contact/', contact_view, name='contact'),
    path('update/<int:pk>', update_post, name='update_post'),
    path('delete/<int:pk>', del_post, name='delete_post'),   
    path('comment/<int:pk>/', new_comment, name='new_comment'),
    path('profile/update/', profile_update, name='profile_update'),
    path('comment/<int:pk>/edit/', comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment_delete'),

]