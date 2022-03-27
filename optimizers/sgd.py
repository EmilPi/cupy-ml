from optimizers.base_optimizer import BaseOptimizer


class SGD(BaseOptimizer):
    def __init__(self, *args, **kwargs):
        # TODO - what is inside super(...) in torch.nn.Module?
        super(SGD, self).__init__(*args, **kwargs)
