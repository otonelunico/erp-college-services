from django.conf.urls import url, include
from .views import QualificationViewSet, \
    QualificationStudent, \
    QualificationStudentDetail, \
    AttorneyList, \
    StudentList, \
    AttorneyDetail, \
    StudentDetail, \
    TeacherList, \
    TeacherDetail, \
    EnrollmentList, \
    EnrollmentDetail, \
    Teacher_SubjectList, \
    Teacher_SubjectTeacher, \
    Teacher_SubjectDetail, \
    GradeList, \
    GradeDetail, \
    StudentDetailId, \
    AttorneyDetailId

from . import views

# quialification
urlpatterns = [
    url(r'^quali/$',QualificationViewSet.as_view(), name='quali'),
    url(r'^quali/(?P<id>[0-9,-]+\d)/$',QualificationStudent.as_view(), name='quali_student'),
    url(r'^quali/(?P<id>[0-9,-]+\d)/(?P<pk>[0-9]+)/$',QualificationStudentDetail.as_view(), name='quali_student_detail'),
]

# teacher_Subject

urlpatterns += [
    url(r'^teacher_subject/$',Teacher_SubjectList.as_view(), name='teacher_Subject_list'),
    url(r'^teacher_subject/(?P<rut>[0-9,-]+\d)/$',Teacher_SubjectTeacher.as_view(), name='teacher_Subject_teacher'),
    url(r'^teacher_subject/(?P<rut>[0-9,-]+\d)/(?P<sub>[0-9]+)/$',Teacher_SubjectDetail.as_view(), name='teacher_subject_detail'),
]

# Person attorney

urlpatterns += [
    url(r'^attorney/$',AttorneyList.as_view(), name='attorney_list'),
    url(r'^attorney/(?P<id>[0-9,-]+\d)/$', AttorneyDetail.as_view(), name='attorney_detail'),
    url(r'^attorney_id/(?P<id>[0-9,-])/$', AttorneyDetailId.as_view(), name='attorney_detail_id'),

]

# Person student

urlpatterns += [
    url(r'^student/$',StudentList.as_view(), name='student_list'),
    url(r'^student/(?P<id>[0-9,-]+\d)/$', StudentDetail.as_view(), name='student_detail'),
    url(r'^student_id/(?P<id>[0-9,-])/$', StudentDetailId.as_view(), name='student_detail_id'),
]

# Person teacher

urlpatterns += [
    url(r'^teacher/$',TeacherList.as_view(), name='teacher_list'),
    url(r'^teacher/(?P<id>[0-9,-]+\d)/$', TeacherDetail.as_view(), name='teacher_detail'),
]

# Person teacher

urlpatterns += [
    url(r'^enrollment/$',EnrollmentList.as_view(), name='enrollment_list'),
    url(r'^enrollment/(?P<id>[0-9]+)/$', EnrollmentDetail.as_view(), name='enrollment_detail'),
]

# Grade

urlpatterns += [
    url(r'^grade/$',GradeList.as_view(), name='grade_list'),
    url(r'^grade/(?P<id>[0-9]+)/$', GradeDetail.as_view(), name='grade_detail'),
    ]

