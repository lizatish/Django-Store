OrdersPostRequest = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'data': {
            'type': 'array',
            'additionalItems': False,
            'minItems': 1,
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'order_id': {
                        'type': 'integer',
                        'minimum': 0
                    },
                    'weight': {
                        'type': 'number',
                        'minimum': 0.01,
                        'maximum': 50
                    },
                    'region': {
                        'type': 'integer',
                        'minimum': 0
                    },
                    'delivery_hours': {
                        'type': 'array',
                        "minItems": 1,
                        'items': {
                            'type': 'interval_time'
                        }
                    }},
                'required': ['order_id', 'weight', 'region', 'delivery_hours']
            }
        }
    },
    'required': ['data']
}
