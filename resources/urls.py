from django.urls import path
from .views import upload_resource
from .views import resource_type_list, resource_type_detail
from .views import upload_page, SignInView
from .views import ResourceListView, ResourceDetailView,SignUpView, SignOutView,UserDashboardView
from .views import (
    create_resource,
    resource_list,
    update_resource,
    delete_resource,
    ResourceListView, ResourceDetailView,
    NoteListView, NoteDetailView,
    EbookListView, EbookDetailView,
    LinkListView, LinkDetailView,
    VideoListView, VideoDetailView,
    ImageListView, ImageDetailView,
    DocumentListView, DocumentDetailView,
)

urlpatterns = [
    path('', ResourceListView.as_view(), name='resource-list'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource-detail'),
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('ebooks/', EbookListView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', EbookDetailView.as_view(), name='ebook-detail'),
    path('links/', LinkListView.as_view(), name='link-list'),
    path('links/<int:pk>/', LinkDetailView.as_view(), name='link-detail'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('images/', ImageListView.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('resource-types/', resource_type_list, name='resource_type_list'),
    path('resource-types/<int:resource_type_id>/', resource_type_detail, name='resource_type_detail'),
    path('create/', create_resource, name='create_resource'),
    path('list/', resource_list, name='resource_list'),
    path('update/<int:resource_id>/', update_resource, name='update_resource'),
    path('delete/<int:resource_id>/', delete_resource, name='delete_resource'),
    path('upload/<int:resource_type_id>/', upload_resource, name='upload_resource'),
    path('upload/page/', upload_page, name='upload_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('dashboard/', UserDashboardView, name='dashboard'),


]   


