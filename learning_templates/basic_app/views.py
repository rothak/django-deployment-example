from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'Hello World', 'number': 100}  # we will use this dict for filter examples
    return render(request, 'basic_app/index.html', context_dict) # we will pass the dict as context parameter

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
