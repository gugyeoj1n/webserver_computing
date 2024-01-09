from django.urls import path, include
from .views import helloAPI, HelloAPI, questionAPI, questionsAPI

urlpatterns = [
    path("fbv/hello/", helloAPI),
    path("cbv/hello/", HelloAPI.as_view()),
    path("fbv/questions/", questionsAPI),
    path("fbv/questions/<int:id>", questionAPI),
]
