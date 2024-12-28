from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    return render(request, "about/about.html", {"about": about, "collaborate_form": collaborate_form},)


def collaborate_form(request):
    """
    Renders the collaboration form in the About page
    """
    if request.method == "POST":
        print("Received a POST request")
        