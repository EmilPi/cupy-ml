class BaseTrainer(object):
    def __init__(self):
        pass

    def train(self, model, train_data_in, train_data_target, optimizer=None, batch_size=32, epochs=4,
              stopping_criteria=None, ):
        self.model = model
        self.train_data_in = train_data_in
        self.train_data_target = train_data_target
        self.optimizer = optimizer
        self.optimizer.bind(model)
        self.epochs = epochs
        self.batch_size = batch_size
        if stopping_criteria is None:
            stopping_criteria = {'valid': ('stall', int(epochs ** .5))}
        self.stopping_criteria = stopping_criteria
