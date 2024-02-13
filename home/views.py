from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import cv

# Create your views here.
def home(requests):
    files = cv.objects.all()
    print(files)
    context = {
        'files' : files
    }
    return render(requests, "home/index.html", context)

def download_cv(request, cv_id):
    cirrirulum_vitae = get_object_or_404(cv, pk=cv_id)
    file_path = cirrirulum_vitae.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{cirrirulum_vitae.title}"'
    return response