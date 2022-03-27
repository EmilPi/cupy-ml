class BaseOptimizer(object):
    def __init__(self, model=None, lr=None, ):
        self.model = model
        self.lr = lr
        pass

    def bind(self, model):
        self.model = model  # TODO
