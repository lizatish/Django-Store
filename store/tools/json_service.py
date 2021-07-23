from django.http import HttpResponse


class JsonService:

    def return_400(self):
        return jsonify(), 400

    def return_404(self):
        return HttpResponse(status=404)

    def return_200(self, data):
        return HttpResponse(data=data)

    def return_201(self, data_type, data):
        success_idxs = [{'id': id} for id in data]
        return jsonify({data_type: success_idxs}), 201

    def __form_400_error_message(self, errors, message):
        errors_idxs = [{'id': error_id} for error_id in errors]
        error_msgs = [{'id': error_id, 'messages': [message]} for error_id in errors]
        return errors_idxs, error_msgs

    def return_courier_logic_error_answer_400(self, errors):
        message = 'Courier with this id already exist'
        error_message_data = self.__form_400_error_message(errors, message)
        return self.__form_400_validation_error('couriers', error_message_data)

    def return_order_logic_error_answer_400(self, errors):
        message = 'Order with this id already exist'
        error_message_data = self.__form_400_error_message(errors, message)
        return self.__form_400_validation_error('orders', error_message_data)

    def return_validation_error_400(self, data_type, data, errors):
        errors_idxs = list()
        error_msgs = list()
        for error in errors:
            if len(error.path) < 2:
                error_msgs.append(error.message)
                break

            error_data_elem = data['data'][error.path[1]]
            if data_type == 'couriers' and 'courier_id' in error_data_elem:
                id = error_data_elem['courier_id']
            elif data_type == 'orders' and 'order_id' in error_data_elem:
                id = error_data_elem['order_id']
            else:
                id = error.path[1] + 1
            error_id = {'id': id}

            if error_id not in errors_idxs:
                errors_idxs.append(error_id)
                error_msgs.append({'id': id, 'messages': [error.message]})
            else:
                error_msgs[-1]['messages'].append(error.message)

        return self.__form_400_validation_error(data_type, (errors_idxs, error_msgs))

    def return_order_assign_200(self, data):
        if not data:
            data = {'orders': []}
            return self.return_200(data)

        orders_idx = [{'id': order.id} for order in data]
        data = {'orders': orders_idx,
                'assign_time':
                    TimeService().get_assign_time(data[0].assign_time)
                }
        return self.return_200(data)

    def __form_400_validation_error(self, data_type, errors_data):
        return jsonify({'validation_error':
                            {data_type: errors_data[0],
                             'error_description':
                                 errors_data[1]}}), 400
