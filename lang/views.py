from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .models import Course

# Create your views here.
def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

def item(request):
    return render(request, 'item.html')


def translate(language):
    cur_language =  get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

