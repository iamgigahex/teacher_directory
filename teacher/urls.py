"""
Teachers  URL configuration.
"""
from django.urls import path, include
from .views import TeacherListView, TeacherDetailsView, BulkUploadView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher_list'),
    path('detail/<int:pk>', TeacherDetailsView.as_view(), name='teacher_details'),
    path('bulk_upload', BulkUploadView.as_view(), name='bulk_upload'),
]