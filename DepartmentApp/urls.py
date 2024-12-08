from django.urls import path
from DepartmentApp import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    # path('department/update/<int:department_id>/', views.update_department, name='update_department'),
    path('createdepartment/',views.createDepartment),
    path('delete/<int:dept_id>',views.Deletedepartment),
    path('edit/<int:did>',views.updateDepartment)

]




