from training.base_trainer import BaseTrainer


class SimpleTrainer(BaseTrainer):
    def __init__(self, *args, **kwargs):
        super(SimpleTrainer, self).__init__(*args, **kwargs)
