from django.http import HttpResponse

def api_home(request):
    return HttpResponse("API Home")

def example_view(request):
    return HttpResponse("Example API View")
