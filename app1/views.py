from django.shortcuts import render, get_object_or_404
from .models import CoverDetails

# Create your views here.
def index(request):
    list_data = CoverDetails.objects.all()
    context = {
        'list_data':list_data
    }
    return render(request, 'app1/index.html', context)

def cover_details(request, pk):
    cover = get_object_or_404(CoverDetails, id=pk)
    
    context = {
        'details': cover
    }
    return render(request, 'app1/cover_detail.html', context)