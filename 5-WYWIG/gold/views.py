from django.shortcuts import render

# Create your views here.
# HOME
def index(request):
    context = {}
    return render(request, 'gold/index.html', context)
