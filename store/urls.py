from django.urls import path

from store.views import CouriersView, OneCourierView

# TODO прочитать, как сделать т
urlpatterns = [
    path('couriers/<int:courier_id>', OneCourierView.as_view()),
    path('couriers', CouriersView.as_view()),

]
