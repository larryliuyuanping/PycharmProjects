# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from maiziserver.tools import views_tools
from maiziserver.db.api.career import career as api_career
from django.http import HttpResponseNotFound,HttpResponseServerError


def get_query(request):

    page = {}
    query = {}
    return {
        "query": query,
        "page": page
    }

def career_query(request):
    query_info = get_query(request)

    result = api_career.list_career()

    if result.is_error():
        return HttpResponseServerError()

    career_list = result.result()["result"]

    context = {
        "menu":"career",
        "url": "/career/",
        "page": {},
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "career_list": career_list
    }

    return context

def career(request):
    context = career_query(request)

    return render(request,'admin/career.html',context)

def career_start(request):

    career_id = views_tools.get_param_by_request(request.GET, "id", "")

    result = api_career.start(career_id)
    if result.is_error():
        return HttpResponseServerError()

    context = career_query(request)
    return render(request,'admin/career.html',context)

def career_stop(request):

    career_id = views_tools.get_param_by_request(request.GET, "id", "")
    result = api_career.stop(career_id)
    if result.is_error():
        return HttpResponseServerError()

    context = career_query(request)
    return render(request, 'admin/career.html', context)

def career_add(request):
    context = {
        "menu": "career"
    }
    return render(request,'admin/career_add.html',context)

@csrf_exempt
def career_add_do(request):

    name = views_tools.get_param_by_request(request.POST, "name", "")
    type = views_tools.get_param_by_request(request.POST, "type", "0")
    remark = views_tools.get_param_by_request(request.POST, "remark", "")

    result = api_career.add(name,type,remark)
    return views_tools.success_json()

def career_update(request):

    career_id = views_tools.get_param_by_request(request.GET, "id")
    result = api_career.get_career_by_id(career_id)

    if result.is_error():
        return HttpResponseServerError()

    career_info = result.result()
    if career_info == None:
        return HttpResponseServerError()

    context = {
        "menu": "career",
        "career": career_info
    }
    return render(request,'admin/career_update.html',context)

@csrf_exempt
def career_update_do(request):

    career_id = views_tools.get_param_by_request(request.POST, "id", "")
    name = views_tools.get_param_by_request(request.POST, "name", "")
    type = views_tools.get_param_by_request(request.POST, "type", "")
    remark = views_tools.get_param_by_request(request.POST, "remark", "")

    result = api_career.update(career_id,name,type,remark)
    return views_tools.success_json()
