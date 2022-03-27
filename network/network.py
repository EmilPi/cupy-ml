from .base_network import BaseNetwork


class Network(BaseNetwork):
    def __init__(self, *args, **kwargs):
        super(Network, self).__init__(*args, **kwargs)

    def compare(self, test_data_in, test_data_out, metric):
        pass
