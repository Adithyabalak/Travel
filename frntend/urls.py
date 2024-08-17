from django.urls import path
from  frntend import views

urlpatterns=[
    path('home_page/',views.home_page,name='home_page'),
    path('about_page/',views.about_page,name='about_page'),
    path('hotel_all/',views.hotel_all,name='hotel_all'),
    path('all_des/',views.all_des,name='all_des'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('save_contact/', views.save_contact, name='save_contact'),
    path('blog_page/', views.blog_page, name='blog_page'),
    path('single_page/<int:pro_id>/', views.single_page, name='single_page'),
    path('all_hotel/<ht_name>/', views.all_hotel, name='all_hotel'),
    path('single_hotel/<int:htlid>/', views.single_hotel, name='single_hotel'),
    path('login_page/', views.login_page, name='login_page'),
    path('', views.register_page, name='register_page'),
    path('save_register/', views.save_register, name='save_register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('booking_page/', views.booking_page, name='booking_page'),
    path('save_booking_hotel/', views.save_booking_hotel, name='save_booking_hotel'),
    path('save_booking_place/', views.save_booking_place, name='save_booking_place'),
    path('delete_booking/<int:dataid>/', views.delete_booking, name="delete_booking"),
    path('delete_place/<int:plcid>/', views.delete_place, name="delete_place"),

    path('payment_page/', views.payment_page, name='payment_page'),
    path('save_payment/', views.save_payment, name='save_payment'),
    path('chatbot_page/', views.chatbot_page, name='chatbot_page'),
    path('re_page/', views.re_page, name='re_page'),
    path('save_reserve/', views.save_reserve, name='save_reserve'),
    path('single_act/<int:actid>/', views.single_act, name='single_act'),
    path('save_act/', views.save_act, name='save_act'),
    path('delete_act/<int:actid>/', views.delete_act, name="delete_act"),

]