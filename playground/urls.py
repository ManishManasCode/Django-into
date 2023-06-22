from django.urls import path
from .views import test_api,test_json_api,test_html_page,test_hello_name,test_html_for_page,home_page,about_page


urlpatterns=[

    # path( "route-name", views, name="name of the route" )
    # name is used for redirection purpose 
    path("test-api/",test_api, name="test_api"),
    path("test_json_api/",test_json_api, name="test_json_api"),
    path("test_html_page/",test_html_page,name="test_html_page"),
    path("test_hello_name/<name>",test_hello_name,name="test_hello_name"),
    path("test_html_for_page/",test_html_for_page,name="test_html_for_page"),
    path("home-page/",home_page, name="home_page"),
    path("about-page/",about_page, name="about_page"),


    ]