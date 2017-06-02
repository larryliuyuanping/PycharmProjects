from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maiziserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^$', 'maiziserver.website.admin.views_user.index',name='index'),
    url(r'^login/$', 'maiziserver.website.admin.views_user.index', name='index'),

    url(r'^user/login/$', 'maiziserver.website.admin.views_user.user_login', name='user_login'),
    url(r'^user/login_out/$', 'maiziserver.website.admin.views_user.user_login_out', name='user_login_out'),

    url(r'^home/$', 'maiziserver.website.admin.views_student.student_sailer', name='student_sailer'),

    url(r'^user/$', 'maiziserver.website.admin.views_user.user', name='user'),
    url(r'^user/start/$', 'maiziserver.website.admin.views_user.user_start', name='user_start'),
    url(r'^user/stop/$', 'maiziserver.website.admin.views_user.user_stop', name='user_stop'),
    url(r'^user/add/$', 'maiziserver.website.admin.views_user.user_add', name='user_add'),
    url(r'^user/add/do/$', 'maiziserver.website.admin.views_user.user_add_do', name='user_add_do'),
    url(r'^user/update/$', 'maiziserver.website.admin.views_user.user_update', name='user_update'),
    url(r'^user/update/do/$', 'maiziserver.website.admin.views_user.user_update_do', name='user_update_do'),

    url(r'^assistant/$', 'maiziserver.website.admin.views_assistant.assistant', name='assistant'),
    url(r'^assistant/start/$', 'maiziserver.website.admin.views_assistant.assistant_start', name='assistant_start'),
    url(r'^assistant/stop/$', 'maiziserver.website.admin.views_assistant.assistant_stop', name='assistant_stop'),
    url(r'^assistant/add/$', 'maiziserver.website.admin.views_assistant.assistant_add', name='assistant_add'),
    url(r'^assistant/add/do/$', 'maiziserver.website.admin.views_assistant.assistant_add_do', name='assistant_add_do'),
    url(r'^assistant/update/$', 'maiziserver.website.admin.views_assistant.assistant_update', name='assistant_update'),
    url(r'^assistant/update/do/$', 'maiziserver.website.admin.views_assistant.assistant_update_do', name='assistant_update_do'),

    url(r'^career/$', 'maiziserver.website.admin.views_career.career', name='career'),
    url(r'^career/start/$', 'maiziserver.website.admin.views_career.career_start', name='career_start'),
    url(r'^career/stop/$', 'maiziserver.website.admin.views_career.career_stop', name='career_stop'),
    url(r'^career/add/$', 'maiziserver.website.admin.views_career.career_add', name='career_add'),
    url(r'^career/add/do/$', 'maiziserver.website.admin.views_career.career_add_do', name='career_add_do'),
    url(r'^career/update/$', 'maiziserver.website.admin.views_career.career_update', name='career_update'),
    url(r'^career/update/do/$', 'maiziserver.website.admin.views_career.career_update_do', name='career_update_do'),

    url(r'^exercise_type/$', 'maiziserver.website.admin.views_exercise_type.exercise_type', name='exercise_type'),
    url(r'^exercise_type/add/$', 'maiziserver.website.admin.views_exercise_type.exercise_type_add', name='exercise_type_add'),
    url(r'^exercise_type/add/do/$', 'maiziserver.website.admin.views_exercise_type.exercise_type_add_do', name='exercise_type_add_do'),
    url(r'^exercise_type/update/$', 'maiziserver.website.admin.views_exercise_type.exercise_type_update', name='exercise_type_update'),
    url(r'^exercise_type/update/do/$', 'maiziserver.website.admin.views_exercise_type.exercise_type_update_do', name='exercise_type_update_do'),


    url(r'^teacher/$', 'maiziserver.website.admin.views_teacher.teacher', name='teacher'),
    url(r'^teacher/start/$', 'maiziserver.website.admin.views_teacher.teacher_start',name='teacher_start'),
    url(r'^teacher/stop/$', 'maiziserver.website.admin.views_teacher.teacher_stop',name='teacher_stop'),
    url(r'^teacher/add/$', 'maiziserver.website.admin.views_teacher.teacher_add',name='teacher_add'),
    url(r'^teacher/add/do/$', 'maiziserver.website.admin.views_teacher.teacher_add_do',name='teacher_add_do'),
    url(r'^teacher/update/$', 'maiziserver.website.admin.views_teacher.teacher_update',name='teacher_update'),
    url(r'^teacher/update/do/$', 'maiziserver.website.admin.views_teacher.teacher_update_do',name='teacher_update_do'),

    url(r'^student_sailer/$', 'maiziserver.website.admin.views_student.student_sailer', name='student_sailer'),
    url(r'^student_sailer/add/$', 'maiziserver.website.admin.views_student.student_sailer_add', name='student_sailer_add'),
    url(r'^student_sailer/add/do/$', 'maiziserver.website.admin.views_student.student_sailer_add_do', name='student_sailer_add_do'),
    url(r'^student_sailer/update/$', 'maiziserver.website.admin.views_student.student_sailer_update', name='student_sailer_update'),
    url(r'^student_sailer/update/do/$', 'maiziserver.website.admin.views_student.student_sailer_update_do',name='student_sailer_update_do'),

    url(r'^student_assistant/$', 'maiziserver.website.admin.views_student.student_assistant', name='student_assistant'),
    url(r'^student_assistant/update/$', 'maiziserver.website.admin.views_student.student_assistant_update',name='student_assistant_update'),
    url(r'^student_assistant/update/do/$','maiziserver.website.admin.views_student.student_assistant_update_do',name='student_assistant_update_do'),

    url(r'^student_assistant_change_teacher/$', 'maiziserver.website.admin.views_student.student_assistant_change_teacher', name='student_assistant_change_teacher'),
    url(r'^student_assistant_change_teacher/add/$', 'maiziserver.website.admin.views_student.student_assistant_change_teacher_add', name='student_assistant_change_teacher_add'),
    url(r'^student_assistant_change_teacher/add/do/$', 'maiziserver.website.admin.views_student.student_assistant_change_teacher_add_do', name='student_assistant_change_teacher_add_do'),

    url(r'^student_assistant_change_assistant/$', 'maiziserver.website.admin.views_student.student_assistant_change_assistant', name='student_assistant_change_assistant'),
    url(r'^student_assistant_change_assistant/add/$', 'maiziserver.website.admin.views_student.student_assistant_change_assistant_add', name='student_assistant_change_assistant_add'),
    url(r'^student_assistant_change_assistant/add/do/$', 'maiziserver.website.admin.views_student.student_assistant_change_assistant_add_do', name='student_assistant_change_assistant_add_do'),

    url(r'^student_assistant_communication/$', 'maiziserver.website.admin.views_student.student_assistant_communication', name='student_assistant_communication'),
    url(r'^student_assistant_communication/add/$', 'maiziserver.website.admin.views_student.student_assistant_communication_add', name='student_assistant_communication_add'),
    url(r'^student_assistant_communication/add/do/$', 'maiziserver.website.admin.views_student.student_assistant_communication_add_do', name='student_assistant_communication_add_do'),
    url(r'^student_assistant_communication/detail/$', 'maiziserver.website.admin.views_student.student_assistant_communication_detail', name='student_assistant_communication_detail'),
    url(r'^student_assistant_communication_all/$', 'maiziserver.website.admin.views_student.student_assistant_communication_all', name='student_assistant_communication_all'),

    url(r'^student_assistant_suspend/$','maiziserver.website.admin.views_student.student_assistant_suspend',name='student_assistant_suspend'),
    url(r'^student_assistant_suspend/add/$', 'maiziserver.website.admin.views_student.student_assistant_suspend_add',name='student_assistant_suspend_add'),
    url(r'^student_assistant_suspend/add/do/$','maiziserver.website.admin.views_student.student_assistant_suspend_add_do',name='student_assistant_suspend_add_do'),
    url(r'^student_assistant_suspend/detail/$','maiziserver.website.admin.views_student.student_assistant_suspend_detail',name='student_assistant_suspend_detail'),
    url(r'^student_assistant_suspend_all/$','maiziserver.website.admin.views_student.student_assistant_suspend_all',name='student_assistant_suspend_all'),


                       url(r'^student_assistant_interview/$', 'maiziserver.website.admin.views_student.student_assistant_interview',name='student_assistant_interview'),
    url(r'^student_assistant_interview/add/$','maiziserver.website.admin.views_student.student_assistant_interview_add',name='student_assistant_interview_add'),
    url(r'^student_assistant_interview/add/do/$','maiziserver.website.admin.views_student.student_assistant_interview_add_do',name='student_assistant_interview_add_do'),
    url(r'^student_assistant_interview/update/$','maiziserver.website.admin.views_student.student_assistant_interview_update',name='student_assistant_interview_update'),
    url(r'^student_assistant_interview/update/do/$','maiziserver.website.admin.views_student.student_assistant_interview_update_do',name='student_assistant_interview_update_do'),

    url(r'^document/$', 'maiziserver.website.admin.views_document.document', name='document'),
    url(r'^document/add/$', 'maiziserver.website.admin.views_document.document_add', name='document_add'),
    url(r'^document/add/do/$', 'maiziserver.website.admin.views_document.document_add_do', name='document_add_do'),

    url(r'^upload/$', 'maiziserver.website.admin.views_common.upload', name='upload'),
    url(r'^add/success/$', 'maiziserver.website.admin.views_common.add_success', name='add_success'),
    url(r'^update/success/$', 'maiziserver.website.admin.views_common.update_success', name='update_success'),

    url(r'^download/document/$', 'maiziserver.website.admin.views_document.download_document', name='download_document'),
    #url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
