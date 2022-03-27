from .base_layer import BaseLayer


class Dense(BaseLayer):
    def __init__(self, *args, **kwargs):
        super(Dense, self).__init__(*args, **kwargs)
