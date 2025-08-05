from django.shortcuts import render

# Create your views here.
def homeLayout(request):
    return render( request, 'layout/sidebar.html', {})