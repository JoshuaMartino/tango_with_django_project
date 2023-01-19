from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}


    return render(request, 'rango/index.html', context=context_dict)

def picture(request):
    context_dict = {'boldmessage': 'This is what i look like'}
    return render(request, 'rango/picture.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page (<a href= '/rango/'>Index</a>)) \n Here is the picture (<a href= '/rango/picture/'>Picture</a>))")


# Create your views here.
