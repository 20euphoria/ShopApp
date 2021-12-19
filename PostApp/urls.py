from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', signupuser, name='signup'),
    path("create_post/", create_post, name="create_post"),
    path("post_detail/<int:id>/", post_detail, name="post_detail"),
    path("delete_post/<int:id>/", delete_post, name="delete_post"),

]
