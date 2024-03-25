from django.urls import path
from . import views

urlpatterns =[

]

from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()  # 可以处理视图的路由器
router.register("stu", viewset=views.StudentModelViewSet, basename="stu") # 向路由器中注册视图集
urlpatterns += router.urls # 将路由器中的所以路由信息追到到django的路由列表中