# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from maiziserver.tools import views_tools
from maiziserver.db.api.student import student as api_student
from maiziserver.db.api.career import career as api_career
from maiziserver.db.api.teacher import teacher as api_teacher
from maiziserver.db.api.assistant import assistant as api_assistant
from django.http import HttpResponseNotFound,HttpResponseServerError

def get_query_sailer(request):

    page_index = views_tools.get_param_by_request(request.GET, "page_index", 1, int)
    page_size = views_tools.get_param_by_request(request.GET, "page_size", 10, int)

    account = views_tools.get_param_by_request(request.GET, "account", "")
    student_name = views_tools.get_param_by_request(request.GET, "student_name", "")
    sailer = views_tools.get_param_by_request(request.GET, "sailer", "")
    phone = views_tools.get_param_by_request(request.GET, "phone", "")
    qq = views_tools.get_param_by_request(request.GET, "qq", "")

    page = {
        "page_index":page_index,
        "page_size":page_size
    }

    query = {
        "account": account,
        "student_name": student_name,
        "sailer": sailer,
        "phone": phone,
        "qq": qq
    }

    return {
             "query":query,
             "page":page
            }

def get_query_assistant(request):

    page_index = views_tools.get_param_by_request(request.GET, "page_index", 1, int)
    page_size = views_tools.get_param_by_request(request.GET, "page_size", 10, int)

    account = views_tools.get_param_by_request(request.GET, "account", "")
    student_name = views_tools.get_param_by_request(request.GET, "student_name", "")
    career_id = views_tools.get_param_by_request(request.GET, "career_id", -1, int)
    career_job = views_tools.get_param_by_request(request.GET, "career_job", -1, int)
    assistant_id = views_tools.get_param_by_request(request.GET, "assistant_id", -1, int)
    teacher_id = views_tools.get_param_by_request(request.GET, "teacher_id", -1, int)
    reward = views_tools.get_param_by_request(request.GET, "reward", -1, int)

    page = {
        "page_index":page_index,
        "page_size":page_size
    }

    query = {
        "account": account,
        "student_name": student_name,
        "career_id": str(career_id),
        "career_job": str(career_job),
        "assistant_id": str(assistant_id),
        "teacher_id": str(teacher_id),
        "reward": str(reward)
    }

    return {
             "query":query,
             "page":page
            }

def get_query_assistant_change(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id", "")
    page = {
    }

    query = {
        "student_id":student_id
    }

    return {
             "query":query,
             "page":page
            }

def get_query_assistant_communication(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id", "")
    page = {
    }

    query = {
        "student_id":student_id
    }

    return {
             "query":query,
             "page":page
            }

def get_query_assistant_communication_all(request):
    page_index = views_tools.get_param_by_request(request.GET, "page_index", 1, int)
    page_size = views_tools.get_param_by_request(request.GET, "page_size", 10, int)

    career_id = views_tools.get_param_by_request(request.GET, "career_id", -1, int)
    assistant_id = views_tools.get_param_by_request(request.GET, "assistant_id", -1, int)

    page = {
        "page_index": page_index,
        "page_size": page_size
    }

    query = {
        "career_id": str(career_id),
        "assistant_id": str(assistant_id)
    }

    return {
        "query": query,
        "page": page
    }

def get_query_assistant_suspend(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id", "")
    page = {
    }

    query = {
        "student_id":student_id
    }

    return {
             "query":query,
             "page":page
            }

def get_query_assistant_suspend_all(request):
    page_index = views_tools.get_param_by_request(request.GET, "page_index", 1, int)
    page_size = views_tools.get_param_by_request(request.GET, "page_size", 10, int)

    career_id = views_tools.get_param_by_request(request.GET, "career_id", -1, int)
    assistant_id = views_tools.get_param_by_request(request.GET, "assistant_id", -1, int)

    page = {
        "page_index": page_index,
        "page_size": page_size
    }

    query = {
        "career_id": str(career_id),
        "assistant_id": str(assistant_id)
    }

    return {
        "query": query,
        "page": page
    }

def get_query_assistant_interview(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id", "")
    page = {
    }

    query = {
        "student_id":student_id
    }

    return {
             "query":query,
             "page":page
            }

def student_sailer_query(request):
    query_info = get_query_sailer(request)

    skip = views_tools.get_skip(query_info["page"]["page_index"], query_info["page"]["page_size"])

    result = api_student.list_student_sailer(query_info["query"]["account"],
                                      query_info["query"]["student_name"],
                                      query_info["query"]["sailer"],
                                      query_info["query"]["phone"],
                                      query_info["query"]["qq"],
                                      skip)
    if result.is_error():
        return HttpResponseServerError()

    rows_count = result.result()["rows_count"]
    student_list = result.result()["result"]

    page = views_tools.get_page(query_info["page"]["page_index"],
                                query_info["page"]["page_size"],
                                rows_count)
    context = {
        "menu": "sailer",
        "url": "/student_sailer/",
        "page": page,
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "student_list": student_list
    }

    def student_sailer_query(request):
        query_info = get_query_sailer(request)

        skip = views_tools.get_skip(query_info["page"]["page_index"], query_info["page"]["page_size"])

        result = api_student.list_student_sailer(query_info["query"]["account"],
                                                 query_info["query"]["student_name"],
                                                 query_info["query"]["sailer"],
                                                 query_info["query"]["phone"],
                                                 query_info["query"]["qq"],
                                                 skip)
        if result.is_error():
            return HttpResponseServerError()

        rows_count = result.result()["rows_count"]
        student_list = result.result()["result"]

        page = views_tools.get_page(query_info["page"]["page_index"],
                                    query_info["page"]["page_size"],
                                    rows_count)
        context = {
            "url": "/student_sailer/",
            "page": page,
            "query": query_info["query"],
            "queryString": views_tools.getQueryString(query_info["query"]),
            "student_list": student_list
        }

    return context

def student_assistant_query(request):
    query_info = get_query_assistant(request)

    skip = views_tools.get_skip(query_info["page"]["page_index"], query_info["page"]["page_size"])
    result = api_student.list_student_assistant(query_info["query"]["account"],
                                      query_info["query"]["student_name"],
                                      query_info["query"]["career_id"],
                                      query_info["query"]["career_job"],
                                      query_info["query"]["assistant_id"],
                                      query_info["query"]["teacher_id"],
                                      query_info["query"]["reward"],
                                      skip)
    if result.is_error():
        return HttpResponseServerError()

    rows_count = result.result()["rows_count"]
    student_list = result.result()["result"]

    page = views_tools.get_page(query_info["page"]["page_index"],
                                query_info["page"]["page_size"],
                                rows_count)

    career_list = api_career.list_career().result()["result"]
    teacher_list = api_teacher.list_teacher().result()["result"]
    assistant_list = api_assistant.list_assistant().result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant/",
        "page": page,
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "student_list": student_list,
        "career_list": career_list,
        "teacher_list": teacher_list,
        "assistant_list": assistant_list
    }

    return context

def student_assistant_change_teacher_query(request):
    query_info = get_query_assistant_change(request)

    result = api_student.list_student_assistant_change_teacher(query_info["query"]["student_id"])
    if result.is_error():
        return HttpResponseServerError()

    log_list = result.result()["result"]

    context = {
        "menu":"assistant",
        "url": "/student_assistant_change_teacher/",
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list
    }

    return context

def student_assistant_change_assistant_query(request):
    query_info = get_query_assistant_change(request)
    result = api_student.list_student_assistant_change_assistant(query_info["query"]["student_id"])
    if result.is_error():
        return HttpResponseServerError()

    log_list = result.result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant_change_teacher/",
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list
    }

    return context

def student_assistant_communication_query(request):
    query_info = get_query_assistant_communication(request)

    result = api_student.list_student_assistant_communication(query_info["query"]["student_id"])
    if result.is_error():
        return HttpResponseServerError()

    log_list = result.result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant_communication/",
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list
    }

    return context

def student_assistant_communication_query_all(request):
    query_info = get_query_assistant_communication_all(request)

    skip = views_tools.get_skip(query_info["page"]["page_index"], query_info["page"]["page_size"])
    result = api_student.list_student_assistant_communication_all(
                                      query_info["query"]["career_id"],
                                      query_info["query"]["assistant_id"],
                                      skip)
    if result.is_error():
        return HttpResponseServerError()

    rows_count = result.result()["rows_count"]
    log_list = result.result()["result"]

    page = views_tools.get_page(query_info["page"]["page_index"],
                                query_info["page"]["page_size"],
                                rows_count)

    career_list = api_career.list_career().result()["result"]
    assistant_list = api_assistant.list_assistant().result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant_communication_all/",
        "page": page,
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list,
        "career_list": career_list,
        "assistant_list": assistant_list
    }

    return context

def student_assistant_suspend_query(request):
    query_info = get_query_assistant_suspend(request)

    result = api_student.list_student_assistant_suspend(query_info["query"]["student_id"])
    if result.is_error():
        return HttpResponseServerError()

    log_list = result.result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant_suspend/",
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list
    }

    return context

def student_assistant_suspend_query_all(request):
    query_info = get_query_assistant_suspend_all(request)

    skip = views_tools.get_skip(query_info["page"]["page_index"], query_info["page"]["page_size"])
    result = api_student.list_student_assistant_suspend_all(
                                      query_info["query"]["career_id"],
                                      query_info["query"]["assistant_id"],
                                      skip)
    if result.is_error():
        return HttpResponseServerError()

    rows_count = result.result()["rows_count"]
    log_list = result.result()["result"]

    page = views_tools.get_page(query_info["page"]["page_index"],
                                query_info["page"]["page_size"],
                                rows_count)

    career_list = api_career.list_career().result()["result"]
    assistant_list = api_assistant.list_assistant().result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant_suspend_all/",
        "page": page,
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list,
        "career_list": career_list,
        "assistant_list": assistant_list
    }

    return context

def student_assistant_interview_query(request):
    query_info = get_query_assistant_interview(request)

    result = api_student.list_student_assistant_interview(query_info["query"]["student_id"])
    if result.is_error():
        return HttpResponseServerError()

    log_list = result.result()["result"]

    context = {
        "menu": "assistant",
        "url": "/student_assistant_interview/",
        "query": query_info["query"],
        "queryString": views_tools.getQueryString(query_info["query"]),
        "log_list": log_list
    }

    return context

def student_sailer(request):
    context = student_sailer_query(request)
    return render(request,'admin/student_sailer.html',context)

def student_assistant(request):

    context = student_assistant_query(request)

    return render(request,'admin/student_assistant.html',context)

def student_assistant_change_teacher(request):
    context = student_assistant_change_teacher_query(request)
    return render(request,'admin/student_assistant_change_teacher.html',context)

def student_assistant_change_assistant(request):
    context = student_assistant_change_assistant_query(request)
    return render(request,'admin/student_assistant_change_assistant.html',context)

def student_assistant_communication(request):

    context = student_assistant_communication_query(request)
    return render(request,'admin/student_assistant_communication.html',context)

def student_assistant_communication_all(request):

    context = student_assistant_communication_query_all(request)
    return render(request,'admin/student_assistant_communication_all.html',context)

def student_assistant_communication_detail(request):
    id = views_tools.get_param_by_request(request.GET, "id")
    result = api_student.get_student_assistant_communication_by_id(id)

    if result.is_error():
        return HttpResponseServerError()

    communication_info = result.result()
    if communication_info == None:
        return HttpResponseServerError()
    context = {
        "menu": "assistant",
        "communication": communication_info
    }
    return render(request, 'admin/student_assistant_communication_detail.html', context)

def student_assistant_suspend(request):

    context = student_assistant_suspend_query(request)
    return render(request,'admin/student_assistant_suspend.html',context)

def student_assistant_suspend_all(request):

    context = student_assistant_suspend_query_all(request)
    return render(request,'admin/student_assistant_suspend_all.html',context)

def student_assistant_suspend_detail(request):
    id = views_tools.get_param_by_request(request.GET, "id")
    result = api_student.get_student_assistant_suspend_by_id(id)

    if result.is_error():
        return HttpResponseServerError()

    suspend_info = result.result()
    if suspend_info == None:
        return HttpResponseServerError()
    context = {
        "menu": "assistant",
        "suspend": suspend_info
    }
    return render(request, 'admin/student_assistant_suspend_detail.html', context)

def student_assistant_interview(request):

    context = student_assistant_interview_query(request)
    return render(request,'admin/student_assistant_interview.html',context)

def student_sailer_add(request):

    career_list = api_career.list_career_can_use().result()["result"]
    teacher_list = api_teacher.list_teacher_can_use().result()["result"]
    assistant_list = api_assistant.list_assistant_can_use().result()["result"]

    context = {
        "menu": "sailer",
        "career_list": career_list,
        "teacher_list": teacher_list,
        "assistant_list": assistant_list,
        "sailer": request.session["real_name"]
    }

    return render(request,'admin/student_sailer_add.html', context)

@csrf_exempt
def student_sailer_add_do(request):

    account = views_tools.get_param_by_request(request.POST, "account", "")
    student_name = views_tools.get_param_by_request(request.POST, "student_name", "")
    phone = views_tools.get_param_by_request(request.POST, "phone", "")
    qq = views_tools.get_param_by_request(request.POST, "qq", "")
    address = views_tools.get_param_by_request(request.POST, "address", "")
    career_id = views_tools.get_param_by_request(request.POST, "career_id", 0)
    career_job = views_tools.get_param_by_request(request.POST, "career_job", 0)
    pay_money = views_tools.get_param_by_request(request.POST, "pay_money", 0)
    pay_type = views_tools.get_param_by_request(request.POST, "pay_type", "")
    sailer = views_tools.get_param_by_request(request.POST, "sailer", "")
    sail_at = views_tools.get_param_by_request(request.POST, "sail_at", "")
    assistant_id = views_tools.get_param_by_request(request.POST, "assistant_id", 0)
    teacher_id = views_tools.get_param_by_request(request.POST, "teacher_id", 0)
    sail_remark = views_tools.get_param_by_request(request.POST, "sail_remark", "")
    student_remark = views_tools.get_param_by_request(request.POST, "student_remark", "")

    reward = views_tools.get_param_by_request(request.POST, "reward", "0")
    reward_month = views_tools.get_param_by_request(request.POST, "reward_month", "0")
    bank = views_tools.get_param_by_request(request.POST, "bank", "")
    bank_account = views_tools.get_param_by_request(request.POST, "bank_account", "")
    idcard = views_tools.get_param_by_request(request.POST, "idcard", "")

    loan= views_tools.get_param_by_request(request.POST, "loan", "")
    loan_company= views_tools.get_param_by_request(request.POST, "loan_company", "")
    loan_type= views_tools.get_param_by_request(request.POST, "loan_type", "")
    loan_interest= views_tools.get_param_by_request(request.POST, "loan_interest", "")
    loan_person= views_tools.get_param_by_request(request.POST, "loan_person", "")
    loan_money= views_tools.get_param_by_request(request.POST, "loan_money", "")
    subsidy= views_tools.get_param_by_request(request.POST, "subsidy", "")
    reduction= views_tools.get_param_by_request(request.POST, "reduction", "")

    result = api_student.sailer_add(account,
                                       student_name,
                                       phone,
                                       qq,
                                       address,
                                       career_id,
                                       career_job,
                                       pay_money,
                                       pay_type,
                                       sailer,
                                       sail_at,
                                       assistant_id,
                                       teacher_id,
                                       sail_remark,
                                       student_remark,
                                        reward,
                                        reward_month,
                                        bank,
                                        bank_account,
                                        idcard,
                                        loan,
                                        loan_company,
                                        loan_type,
                                        loan_interest,
                                        loan_person,
                                        loan_money,
                                        subsidy,
                                        reduction
                                    )
    return views_tools.success_json()

def student_sailer_update(request):
    student_id = views_tools.get_param_by_request(request.GET, "id")

    career_list = api_career.list_career_can_use().result()["result"]
    teacher_list = api_teacher.list_teacher_can_use().result()["result"]
    assistant_list = api_assistant.list_assistant_can_use().result()["result"]

    result = api_student.get_student_by_id(student_id)

    if result.is_error():
        return HttpResponseServerError()

    student_info = result.result()
    if student_info == None:
        return HttpResponseServerError()
    context = {
        "menu": "sailer",
        "student": student_info,
        "career_list":career_list,
        "teacher_list":teacher_list,
        "assistant_list":assistant_list
    }
    return render(request,'admin/student_sailer_update.html',context)

@csrf_exempt
def student_sailer_update_do(request):

    student_id = views_tools.get_param_by_request(request.POST, "id", "")
    account = views_tools.get_param_by_request(request.POST, "account", "")
    student_name = views_tools.get_param_by_request(request.POST, "student_name", "")
    phone = views_tools.get_param_by_request(request.POST, "phone", "")
    qq = views_tools.get_param_by_request(request.POST, "qq", "")
    address = views_tools.get_param_by_request(request.POST, "address", "")
    career_id = views_tools.get_param_by_request(request.POST, "career_id", 0)
    career_job = views_tools.get_param_by_request(request.POST, "career_job", 0)
    pay_money = views_tools.get_param_by_request(request.POST, "pay_money", 0)
    pay_type = views_tools.get_param_by_request(request.POST, "pay_type", "")
    sailer = views_tools.get_param_by_request(request.POST, "sailer", "")
    sail_at = views_tools.get_param_by_request(request.POST, "sail_at", "")
    assistant_id = views_tools.get_param_by_request(request.POST, "assistant_id", 0)
    teacher_id = views_tools.get_param_by_request(request.POST, "teacher_id", 0)
    sail_remark = views_tools.get_param_by_request(request.POST, "sail_remark", "")
    student_remark = views_tools.get_param_by_request(request.POST, "student_remark", "")

    reward = views_tools.get_param_by_request(request.POST, "reward", "0")
    reward_month = views_tools.get_param_by_request(request.POST, "reward_month", "0")
    bank = views_tools.get_param_by_request(request.POST, "bank", "")
    bank_account = views_tools.get_param_by_request(request.POST, "bank_account", "")
    idcard = views_tools.get_param_by_request(request.POST, "idcard", "")

    loan= views_tools.get_param_by_request(request.POST, "loan", "")
    loan_company= views_tools.get_param_by_request(request.POST, "loan_company", "")
    loan_type= views_tools.get_param_by_request(request.POST, "loan_type", "")
    loan_interest= views_tools.get_param_by_request(request.POST, "loan_interest", "")
    loan_person= views_tools.get_param_by_request(request.POST, "loan_person", "")
    loan_money= views_tools.get_param_by_request(request.POST, "loan_money", "")
    subsidy= views_tools.get_param_by_request(request.POST, "subsidy", "")
    reduction= views_tools.get_param_by_request(request.POST, "reduction", "")

    result = api_student.sailer_update(student_id,
                                       account,
                                       student_name,
                                       phone,
                                       qq,
                                       address,
                                       career_id,
                                       career_job,
                                       pay_money,
                                       pay_type,
                                       sailer,
                                       sail_at,
                                       assistant_id,
                                       teacher_id,
                                       sail_remark,
                                       student_remark,
                                       reward,
                                       reward_month,
                                       bank,
                                       bank_account,
                                       idcard,
                                       loan,
                                       loan_company,
                                       loan_type,
                                       loan_interest,
                                       loan_person,
                                       loan_money,
                                       subsidy,
                                       reduction
                                       )
    return views_tools.success_json()

def student_assistant_update(request):
    student_id = views_tools.get_param_by_request(request.GET, "id")

    result = api_student.get_student_by_id(student_id)

    if result.is_error():
        return HttpResponseServerError()

    student_info = result.result()
    if student_info == None:
        return HttpResponseServerError()
    context = {
        "menu": "assistant",
        "student": student_info
    }
    return render(request,'admin/student_assistant_update.html',context)

@csrf_exempt
def student_assistant_update_do(request):

    student_id = views_tools.get_param_by_request(request.POST, "id", "")
    start_at = views_tools.get_param_by_request(request.POST, "start_at", "")
    graduate_at = views_tools.get_param_by_request(request.POST, "graduate_at", "")
    stage = views_tools.get_param_by_request(request.POST, "stage", "")
    state = views_tools.get_param_by_request(request.POST, "state", "")
    company = views_tools.get_param_by_request(request.POST, "company", "")

    result = api_student.assistant_update(student_id,
                                       start_at,
                                       graduate_at,
                                       stage,
                                       state,
                                       company
                                       )
    return views_tools.success_json()

def student_assistant_change_teacher_add(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id")
    teacher_list = api_teacher.list_teacher_can_use().result()["result"]
    student = api_student.get_student_by_id(student_id).result()
    context = {
        "menu": "assistant",
        "student_id": student_id,
        "teacher_list": teacher_list,
        "student" : student
    }
    return render(request, 'admin/student_assistant_change_teacher_add.html', context)

@csrf_exempt
def student_assistant_change_teacher_add_do(request):

    student_id = views_tools.get_param_by_request(request.POST, "student_id", "")
    old_teacher_id = views_tools.get_param_by_request(request.POST, "old_teacher_id", "")
    new_teacher_id = views_tools.get_param_by_request(request.POST, "new_teacher_id", "")
    change_at = views_tools.get_param_by_request(request.POST, "change_at", "")
    reason =  views_tools.get_param_by_request(request.POST, "reason", "")

    result = api_student.change_teacher(student_id,
                                        old_teacher_id,
                                        new_teacher_id,
                                        change_at,
                                        reason,
                                        request.session["real_name"])
    return views_tools.success_json()

def student_assistant_change_assistant_add(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id")
    assistant_list = api_assistant.list_assistant_can_use().result()["result"]
    student = api_student.get_student_by_id(student_id).result()
    context = {
        "menu": "assistant",
        "student_id": student_id,
        "assistant_list": assistant_list,
        "student" : student
    }
    return render(request, 'admin/student_assistant_change_assistant_add.html', context)

@csrf_exempt
def student_assistant_change_assistant_add_do(request):

    student_id = views_tools.get_param_by_request(request.POST, "student_id", "")
    old_assistant_id = views_tools.get_param_by_request(request.POST, "old_assistant_id", "")
    new_assistant_id = views_tools.get_param_by_request(request.POST, "new_assistant_id", "")
    change_at = views_tools.get_param_by_request(request.POST, "change_at", "")
    reason =  views_tools.get_param_by_request(request.POST, "reason", "")


    result = api_student.change_assistant(student_id,
                                        old_assistant_id,
                                        new_assistant_id,
                                        change_at,
                                        reason,
                                        request.session["real_name"])
    return views_tools.success_json()

def student_assistant_communication_add(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id")
    assistant_list = api_assistant.list_assistant_can_use().result()["result"]
    context = {
        "assistant_list" : assistant_list,
        "student_id" : student_id,
        "menu": "assistant"
    }
    return render(request, 'admin/student_assistant_communication_add.html', context)

@csrf_exempt
def student_assistant_communication_add_do(request):

    student_id = views_tools.get_param_by_request(request.POST, "student_id", "")
    assistant_id = views_tools.get_param_by_request(request.POST, "assistant_id", "")
    stage = views_tools.get_param_by_request(request.POST, "stage", "")
    communicate_at = views_tools.get_param_by_request(request.POST, "communicate_at", "")
    content =  views_tools.get_param_by_request(request.POST, "content", "")

    result = api_student.add_communication(student_id,
                                           assistant_id,
                                           stage,
                                           communicate_at,
                                           content

                                        )
    return views_tools.success_json()

def student_assistant_suspend_add(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id")
    assistant_list = api_assistant.list_assistant_can_use().result()["result"]
    context = {
        "assistant_list" : assistant_list,
        "student_id" : student_id,
        "menu": "assistant"
    }
    return render(request, 'admin/student_assistant_suspend_add.html', context)

@csrf_exempt
def student_assistant_suspend_add_do(request):
    print ("bbbbbbbbbbbbb")
    student_id = views_tools.get_param_by_request(request.POST, "student_id", "")
    assistant_id = views_tools.get_param_by_request(request.POST, "assistant_id", "")
    start_at = views_tools.get_param_by_request(request.POST, "start_at", "")
    end_at = views_tools.get_param_by_request(request.POST, "end_at", "")
    reason = views_tools.get_param_by_request(request.POST, "reason", "")

    result = api_student.add_suspend(student_id,
                                     assistant_id,
                                     start_at,
                                     end_at,
                                     reason
                                        )
    return views_tools.success_json()

def student_assistant_interview_add(request):

    student_id = views_tools.get_param_by_request(request.GET, "student_id")
    context = {
        "student_id" : student_id,
        "menu": "assistant"
    }
    return render(request, 'admin/student_assistant_interview_add.html', context)

@csrf_exempt
def student_assistant_interview_add_do(request):

    student_id = views_tools.get_param_by_request(request.POST, "student_id", "")
    interviewer = views_tools.get_param_by_request(request.POST, "interviewer", "")
    interview_at = views_tools.get_param_by_request(request.POST, "interview_at", "")
    state = views_tools.get_param_by_request(request.POST, "state", "")
    remark =  views_tools.get_param_by_request(request.POST, "remark", "")

    result = api_student.add_interview(student_id,
                                       interviewer,
                                       interview_at,
                                       state,
                                       remark
                                        )
    return views_tools.success_json()

def student_assistant_interview_update(request):

    id = views_tools.get_param_by_request(request.GET, "id","")
    result = api_student.get_student_assistant_interview_by_id(id)
    print result.result()
    if result.is_error():
        return HttpResponseServerError()

    log = result.result()
    if log == None:
        return HttpResponseServerError()
    context = {
        "menu": "assistant",
        "log": log
    }
    return render(request, 'admin/student_assistant_interview_update.html', context)

@csrf_exempt
def student_assistant_interview_update_do(request):

    id = views_tools.get_param_by_request(request.POST, "id", "")
    interviewer = views_tools.get_param_by_request(request.POST, "interviewer", "")
    interview_at = views_tools.get_param_by_request(request.POST, "interview_at", "")
    state = views_tools.get_param_by_request(request.POST, "state", "")
    remark =  views_tools.get_param_by_request(request.POST, "remark", "")
    result = api_student.update_interview(id,
                                       interviewer,
                                       interview_at,
                                       state,
                                       remark
                                        )
    return views_tools.success_json()

