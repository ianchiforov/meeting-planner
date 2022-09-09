from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request, "my_meeting_planner_app/welcome.html",
                  {
                      "meetings": Meeting.objects.all()
                  })


def date(request):
    return HttpResponse(f"This page was served at {datetime.now()}")


def about(request):
    return HttpResponse("This is about page for my meeting planner...")
