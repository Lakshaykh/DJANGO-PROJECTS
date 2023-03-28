#i have created
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("home")

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc== "on":
        # analyzed=djtext 
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("ERROR")
    # def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlineremover(request):
#     return HttpResponse("new line remover")

# def spaceremover(request):
#     return HttpResponse("space remover <a href ='/'>back </a>")

# def charcount(request):
#     return HttpResponse("chararcter count")


