from django.db import models


class CourierType(models.TextChoices):
    FOOT = "foot"
    BIKE = "bike"
    CAR = "car"

    @staticmethod
    def get_type(type):
        if type == 'foot':
            return CourierType.FOOT
        elif type == 'bike':
            return CourierType.BIKE
        elif type == 'car':
            return CourierType.CAR

    @staticmethod
    def get_max_weight(type):
        if type == CourierType.FOOT:
            return 10
        elif type == CourierType.BIKE:
            return 15
        elif type == CourierType.CAR:
            return 50

    @staticmethod
    def get_coefficient(type):
        if type == CourierType.FOOT:
            return 2
        elif type == CourierType.BIKE:
            return 5
        elif type == CourierType.CAR:
            return 9
