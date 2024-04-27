from mmengine.optim import OptimWrapper

from template.registry import OPTIM_WRAPPERS


@OPTIM_WRAPPERS.register_module()
class CustomOptimWrapper(OptimWrapper):
  ...
