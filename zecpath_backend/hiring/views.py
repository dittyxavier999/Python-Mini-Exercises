import json

from django.http import HttpResponse, JsonResponse
from .models import Job


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