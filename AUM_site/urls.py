"""AUM_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aum import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paramhome, name='home'),
    path('programs/<int:program_id>', views.program, name='programs'),
    path('pages/<str:page_id>', views.pages, name='pages'),
    path('faculty/<int:prof_id>', views.professors, name='professors'),
    path('content/<str:page_id>', views.generalpages, name='content'),
    path('blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#,path('programs/<int:program_id>', views.program, name='programs')