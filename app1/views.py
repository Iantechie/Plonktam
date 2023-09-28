from django.shortcuts import render
from .models import CoverDetails
# Create your views here.
def index(request):
    list_data = CoverDetails.objects.all()
    context = {
        'list_data':list_data
    }
    return render(request, 'app1/index.html', context)