from django.shortcuts import render
from django.http import FileResponse

from result.models import Result

# Create your views here.

def resultSearchPage(request):
    return render(request, "user-view/results/resultSearchPage.html")

def resultView(request):
    if request.method == "POST":
        regNumber = request.POST['registerNumber']
        resultObject = Result.objects.filter(userid = regNumber)
        return render(request,'user-view/results/resultPage.html', {'resultObject': resultObject})


def sslcResultPage(request):
    return render(request, "user-view/results/sslcResultPage.html")

def sslcResultStats(request):
    return render(request, "user-view/results/resultStats.html")

def downloadPoster(request):
    return FileResponse(open('templates/user-view/results/sslc-2022.pdf', 'rb'), content_type='application/pdf')
