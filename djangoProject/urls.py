
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from djangoProject.views import landing_page

from problems.views import problem_list,problem_detail
from submissions.views import submit_code, submission_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    # path('home/', home, name='home'),
    path('users/', include('users.urls'), name='users'),
    path('', include('problems.urls'), name='problems'),
    path('', include('submissions.urls'), name='submissions'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)