from torch.optim import Optimizer

from template.registry import OPTIMIZERS


@OPTIMIZERS.register_module()
class CustomOptimizer(Optimizer):
  ...
