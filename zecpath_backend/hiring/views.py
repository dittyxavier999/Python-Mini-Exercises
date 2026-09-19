import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse, JsonResponse
from .models import Job
from .serializers import JobSerializer

def home(request):
    return HttpResponse("Welcome to Zecpath Hiring API")


def jobs(request):

    if request.method == "GET":
        jobs = Job.objects.all()

        data = []

        for job in jobs:
            data.append({
                "id": job.id,
                "title": job.title,
                "description": job.description,
                "created_at": job.created_at,
            })

        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)

        job = Job.objects.create(
            title=data["title"],
            description=data["description"]
        )

        return JsonResponse({
            "id": job.id,
            "title": job.title,
            "description": job.description,
            "created_at": job.created_at,
        })

class JobListAPIView(APIView):

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class UserTestAPIView(APIView):

    def get(self, request):
        return Response(
            {
                "message": "User API is working",
                "user": "Test User"
            },
            status=status.HTTP_200_OK
        )