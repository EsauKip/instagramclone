from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.display_home,name='home'),
    path('posts/',views.new_post, name='post'),
    path('comment/<int:id>', views.add_comment, name='comment'),
    path('search/',views.search, name='search'),
    path('profile/',views.show_profile, name='profile'),
    path('update/<int:id>',views.update_profile,name='update_profile'),
    path('signup/', views.signup, name='signup'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)