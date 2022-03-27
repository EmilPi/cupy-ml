import numpy as np

from layers import Dense, Activation
from network import Network
from optimizers import SGD
from training import SimpleTrainer

if __name__ == '__main__':
    fc_net = Network(
        Dense(4),
        Activation('tanh'),
        Dense(1),
        input_size=(4,)
    )

    train_data_in = np.random.uniform(size=(64, 4))
    train_data_target = np.random.uniform(size=(64,))
    test_data_in = np.random.uniform(size=(64, 4))
    test_data_target = np.random.uniform(size=(64,))

    optimizer = SGD(lr=1e-3)
    trainer = SimpleTrainer()

    trainer.train(fc_net,
                  train_data_in,
                  train_data_target,
                  optimizer=optimizer,
                  batch_size=4,
                  epochs=64,
                  stopping_criteria={'valid': ('stall', 4)},
                  )

    metric = fc_net.eval(test_data_in, test_data_target, metric='meansq')
    print(metric)
