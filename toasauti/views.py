import requests
import json
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from toasauti.models import Report, Feedback
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def home(request):
    return render(request, 'toasauti/index.html', context={})


def new_report(request):
    return render(request, 'toasauti/new_report.html', context={})


def create_report(request):
    if request.method == 'POST':
        obj = Report()

        images = request.FILES.getlist('image')
        videos = request.FILES.getlist('video')
        audios = request.FILES.getlist('audio')

        obj.carRegNo = request.POST["carRegNo"]
        obj.vehicleType = request.POST["vehicleType"]
        obj.offenceType = request.POST["offenceType"]
        obj.offenceDescription = request.POST["offenceDescription"]
        obj.location = request.POST["location"]
        obj.time = request.POST["date"]

        if images is not None:
            for i in images:
                obj.image = i

        if videos is not None:
            for v in videos:
                obj.video = v

        if audios is not None:
            for a in audios:
                obj.audio = a

        obj.userNames = request.POST["userNames"]
        obj.userIDNumber = request.POST["userIDNumber"]
        obj.userPhoneNumber = request.POST["userPhoneNumber"]
        obj.userEmail = request.POST["userEmail"]

        obj.save()

        return render(request, 'toasauti/thankyou.html', context={'names': obj.userNames})


@api_view(['GET', 'POST'])
def ussd(request):
    if request.method == 'POST':
        # Read the variables sent via POST from Africa's Talking
        received_json_data = json.loads(request.body.decode("utf-8"))
        sessionId = received_json_data["sessionId"]
        serviceCode = received_json_data["serviceCode"]
        phoneNumber = received_json_data["phoneNumber"]
        text = received_json_data["text"]

        if text == "":
            response = "CON Welcome to toa sauti. Type 1 to submit a report"
            # response_j = JsonResponse({'response': response})
            return Response(response, status=status.HTTP_200_OK)

        elif text == "1":
            response = "Enter the Number Plate without spaces. EG KAA001A"
            return Response(response, status=status.HTTP_200_OK)

        elif 1 < len(text) < 8:
            text = str(text)
            respons = " Number plate "+text
            response = "Enter the offence type"

            return Response(respons, status=status.HTTP_200_OK)

        elif 7 < len(text) < 20:
            text = str(text)
            response = "Offence is "+text[8:]
            return Response(response, status=status.HTTP_200_OK)

    else:
        return Response("We ran into an error", status=status.HTTP_404_NOT_FOUND)


def about(request):
    return render(request, 'toasauti/about.html', context={})


def create_feedback(request):
    if request.method == 'POST':
        fb = Feedback()

        fb.firstName = request.POST['firstName']
        fb.lastName = request.POST['lastName']
        fb.message = request.POST['message']
        fb.email = request.POST['email']

        fb.save()

        return render(request, 'toasauti/thankyou.html', context={'names': fb.firstName})
    else:
        message = "There was an error submitting your feedback"
        return render(request, 'toasauti/error.html', context={'message': message})
