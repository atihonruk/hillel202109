from django.urls import path

import blog.views as blog_views


urlpatterns = [
    path('posts/<slug>', blog_views.PostDetail.as_view(), name='post'),
    path('', blog_views.PostList.as_view(), name='post_list'),
]
