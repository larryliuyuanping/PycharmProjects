# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from maiziserver.tools import views_tools
from maiziserver.db.api.exercise import exercise_type as api_exercise_type
from django.http import HttpResponseNotFound,HttpResponseServerError

def get_query(request):

    exercise_type = views_tools.get_param_by_request(request.GET, "exercise_type", "")

    page = {
    }

    query = {
        "exercise_type": exercise_type
    }

    return {
        "query": query,
        "page": page
    }

def exercise_type_query(request):
    query_info = get_query(request)
    print("xxxxxxxxxxx")
    result = api_exercise_type.list_exercise_type(query_info["query"]["exercise_type"])

    if result.is_error():
        return HttpResponseServerError()

    exercise_type_list = result.result()["result"]

    context = {
        "menu":"exercise_type",
        "url": "/exercise_type/",
        "page": {},
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "exercise_type_list": exercise_type_list
    }

    return context

def exercise_type(request):
    context = exercise_type_query(request)
    return render(request,'admin/exercise_type.html',context)

def exercise_type_add(request):
    context = {
        "menu": "exercise_type"
    }
    return render(request,'admin/exercise_type_add.html',context)

@csrf_exempt
def exercise_type_add_do(request):

    exercise_type = views_tools.get_param_by_request(request.POST, "exercise_type", "")

    result = api_exercise_type.add(exercise_type)
    return views_tools.success_json()

def exercise_type_update(request):

    exercise_type_id = views_tools.get_param_by_request(request.GET, "id")
    result = api_exercise_type.get_exercise_type_by_id(exercise_type_id)

    if result.is_error():
        return HttpResponseServerError()

    exercise_type_info = result.result()
    if exercise_type_info == None:
        return HttpResponseServerError()

    context = {
        "menu": "exercise_type",
        "exercise_type": exercise_type_info
    }
    return render(request,'admin/exercise_type_update.html',context)

@csrf_exempt
def exercise_type_update_do(request):

    exercise_type_id = views_tools.get_param_by_request(request.POST, "id", "")
    exercise_type = views_tools.get_param_by_request(request.POST, "exercise_type", "")

    result = api_exercise_type.update(exercise_type_id, exercise_type)
    return views_tools.success_json()