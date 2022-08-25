from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse("Welcome to my meeting planner!")


def date(request):
    return HttpResponse(f"This page was served at {datetime.now()}")


def about(request):
    return HttpResponse("This is about page for my meeting planner...")
