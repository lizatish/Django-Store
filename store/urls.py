from django.urls import path

from store.views import CourierView

# TODO прочитать, как сделать т
urlpatterns = [
    path('couriers/<int:courier_id>',  CourierView.as_view()),
    path('couriers', CourierView.as_view()),

]
