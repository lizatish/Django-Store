from datetime import datetime

import jsonschema

from store.shemas.courier_id import CourierId
from store.shemas.courier_item import CourierItem
from store.shemas.courier_post_request import CouriersPostRequest
from store.shemas.order_complete import OrderComplete
from store.shemas.order_post_request import OrdersPostRequest


class Validator:
    def __init__(self):
        self.validator = jsonschema.Draft7Validator

    def check_post_couriers_validation(self, data):
        errors = self.__create_base_validator(data, CouriersPostRequest, interval_time_checker=True)
        return errors

    def check_post_orders_validation(self, data):
        errors = self.__create_base_validator(data, OrdersPostRequest, interval_time_checker=True)
        return errors

    def check_get_courier_validation(self, data):
        errors = self.__create_base_validator(data, CourierItem, interval_time_checker=True)
        return errors

    def check_post_orders_assign_validation(self, data):
        errors = self.__create_base_validator(data, CourierId)
        return errors

    def check_post_orders_complete(self, data):
        errors = self.__create_base_validator(data, OrderComplete, format_checker=jsonschema.FormatChecker())
        return errors

    def __create_base_validator(self, data, schema, format_checker=None, interval_time_checker=False):

        def is_time_interval(checker, inst):
            try:
                if not isinstance(inst, str):
                    raise ValueError
                date = inst.split('-')
                if len(date) != 2:
                    raise ValueError
                datetime.strptime(date[0], '%H:%M')
                datetime.strptime(date[1], '%H:%M')
                return True
            except ValueError:
                return False

        interval_time_check = None
        if interval_time_checker:
            interval_time_check = self.validator.TYPE_CHECKER.redefine(u'interval_time', is_time_interval)

        validator = jsonschema.validators.extend(self.validator, type_checker=interval_time_check)
        return list(validator(schema=schema, format_checker=format_checker).iter_errors(data))
