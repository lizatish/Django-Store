from django.urls import path

from store.views import CourierView

urlpatterns = [
    path('couriers/<int:courier_id>',  CourierView.as_view()),
]
