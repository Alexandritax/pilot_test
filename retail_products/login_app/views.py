from django.shortcuts import render

# Create your views here.

def print_world(request):

    text_p = 'hello world'

    return render(request, 'hello_world.html' ,{'text_p' : text_p})