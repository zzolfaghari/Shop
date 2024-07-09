class ProductVO:
    image = 'image'
    product_tag = 'Product'
    image_set = 'image_set'
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
    title = 'title'
    description = 'description'
    price = 'price'

