from django.urls import path

from .views import(
    post_create_view,
    post_detail_view,
    post_list_view,
    post_update_view,
    post_delete_view,
    post_like_view,
    post_comments_view
)

app_name='posts';


urlpatterns=[
    path('create/',post_create_view, name='create'),
    path('detail/<int:id>',post_detail_view, name='detail'),
    path('list/',post_list_view, name='list'),
    path('update/<int:id>',post_update_view, name='update'),
    path('delete/<int:id>',post_delete_view, name='delete'),
    path('like/<int:id>',post_like_view,name='like'),
    path('detail/<int:id>/comment/',post_comments_view,name='comment')
]
