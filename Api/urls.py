from django.conf.urls import url, include
from .views import QualificationViewSet, \
    QualificationStudent, \
    QualificationStudentDetail, \
    Teacher_SubjectList, \
    AttorneyList, \
    StudentList, \
    AttorneyDetail, \
    StudentDetail
from . import views

# Normal Url
urlpatterns = [
    url(r'^quali/$',QualificationViewSet.as_view(), name='quali'),
    url(r'^quali/(?P<id>[0-9,-]+\d)/$',QualificationStudent.as_view(), name='quali_student'),
    url(r'^quali/(?P<id>[0-9,-]+\d)/(?P<pk>[0-9]+)/$',QualificationStudentDetail.as_view(), name='quali_student_detail'),
]

# teacher_Subject

urlpatterns += [
    url(r'^teacher_subject/$',Teacher_SubjectList.as_view(), name='teacher_Subject'),
]

# Person attorney

urlpatterns += [
    url(r'^attorney/$',AttorneyList.as_view(), name='attorney'),
    url(r'^attorney/(?P<id>[0-9,-]+\d)/$', AttorneyDetail.as_view(), name='attorney_detail'),

]

# Person student

urlpatterns += [
    url(r'^student/$',StudentList.as_view(), name='attorney'),
    url(r'^student/(?P<id>[0-9,-]+\d)/$', StudentDetail.as_view(), name='student_detail'),
]