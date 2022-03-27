from .base_layer import BaseLayer


class Activation(BaseLayer):
    def __init__(self, *args, **kwargs):
        super(Activation, self).__init__(*args, **kwargs)
