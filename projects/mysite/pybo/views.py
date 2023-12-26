from django.http import HttpResponse

def index(req) :
    return HttpResponse("앙 김옥지~")

def test(req) :
    return HttpResponse("테스트임")