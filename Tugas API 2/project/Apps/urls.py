from django.urls import path
from myFirstApp import views
from myFirstApp import views_api

app_name = "myFirstApp"
urlpatterns = [
    path('', views.home, name='home'),
    path('read/', views.readStudent, name='read-data-student'),
    path('create/', views.createStudent, name='create-data-student'),
    path('update/<str:id>', views.updateStudent, name='update-data-student'),
    path('delete/<str:id>', views.deleteStudent, name='delete-data-student'),

    # URLs untuk Course
    path('read/course', views.readCourse, name='read-data-course'),
    path('create/course', views.createCourse, name='create-data-course'),
    path('update/course/<str:id>', views.updateCourse, name='update-data-course'),
    path('delete/course/<str:id>', views.deleteCourse, name='delete-data-course'),

    # URLs untuk API Course
    path('api/course', views_api.apiCourse, name='api-view-data-course'),

    # URLs untuk Consume API
    path('api/consume/course', views_api.consumeApiGet, name='api-consume-get-data'),
    path('api/consume/course/post', views_api.consumeApiPost, name='api-consume-post-data'),
    path('api/consume/course/put/<str:id>', views_api.consumeApiPut, name='api-consume-put-data'),
]
