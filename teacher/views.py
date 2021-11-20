from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, View

from teacher.forms import BulkUploadForm
from teacher.models import Teacher, Subject
from teacher.utility import Utilities


class TeacherListView(ListView):
    model = Teacher
    form_class = BulkUploadForm
    extra_context = {
        'bulk_upload_form': form_class,
        'subjects': Subject.objects.all()
    }
    template_name = "teacher_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_params = {}
        last_name_search = self.request.GET.get('last_name', '').strip()
        subject_search = self.request.GET.get('subject')
        if last_name_search or subject_search:
            if last_name_search:
                filter_params['last_name__istartswith'] = last_name_search
            if subject_search:
                filter_params['subjects__name'] = subject_search
            return queryset.filter(**filter_params)
        return queryset


class TeacherDetailsView(DetailView):
    model = Teacher
    template_name = "teacher_details.html"


@method_decorator(login_required, name='dispatch')
class BulkUploadView(View):
    form_class = BulkUploadForm
    success_url = reverse_lazy('teacher_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        success, failed = Utilities.upload_from_csv(request.FILES['csv_file'], request.FILES['image_zipfile'])
        if success:
            messages.success(request, f'Successfully uploaded {success} entries')
        if failed:
            messages.error(request, f'Fail to upload {failed} entries')
        return HttpResponseRedirect(reverse_lazy('teacher_list'))
