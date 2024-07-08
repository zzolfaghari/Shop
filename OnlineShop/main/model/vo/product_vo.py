class ProductVO:
    image = 'image'
    product_tag = 'Product'
    update_or_create_product_request_schema = {
                'type': 'object',
                'properties': {
                    'image': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'format': 'binary'
                        }
                    },
                    'title': {
                        'type': 'string'
                    },
                    'description': {
                        'type': 'string'
                    },
                    'price': {
                        'type': 'number',
                        'format': 'decimal'
                    },

                },
                'required': ['title', 'description', 'price'],
            }

