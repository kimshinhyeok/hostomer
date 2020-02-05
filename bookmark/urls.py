
from django.urls import path
from .views import BookmarkList, BookmarkCreate, BookmarkDelete, BookmarkUpdate, BookmarkDetail


app_name = 'bookmark'

urlpatterns = [
    path('create/', BookmarkCreate.as_view(), name='create'),
    path('detail/<int:pk>', BookmarkDetail.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDelete.as_view(), name='delete'),
    path('', BookmarkList.as_view(), name='index'),
]
