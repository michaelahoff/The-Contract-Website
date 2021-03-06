from django.conf.urls import url
from profiles.views import ProfileView, my_profile_view, profile_edit, accept_terms

app_name = 'profiles'
urlpatterns = [
    # ex: .com/profile/view/21/
    url(r'^view/(?P<pk>[\d]+)/$', ProfileView.as_view(), name='profiles_view_profile'),

    # ex: .com/profile/view/me/
    url(r'^view/me/$', my_profile_view, name='profiles_view_my_profile'),

    # ex: .com/profile/edit
    url(r'^edit/$', profile_edit, name='profiles_edit'),

    # ex: .com/profile/terms/
    url(r'^terms/$', accept_terms, name='profiles_terms'),
]