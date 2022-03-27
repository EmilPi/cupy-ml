class BaseNetwork(object):
    def __init__(self, *args, **kwargs):
        pass

    def train(self, train_data_in, train_data_out, epochs=-1):
        pass

    def eval(self, test_data_in, test_data_target, metric):
        pass
