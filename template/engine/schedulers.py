from mmengine.optim import _ParamScheduler
from mmengine.optim.scheduler.lr_scheduler import LRSchedulerMixin
from mmengine.optim.scheduler.momentum_scheduler import MomentumSchedulerMixin

from template.registry import PARAM_SCHEDULERS


@PARAM_SCHEDULERS.register_module()
class CustomParameterScheduler(_ParamScheduler):
  ...


@PARAM_SCHEDULERS.register_module()
class CustomLRScheduler(LRSchedulerMixin, CustomParameterScheduler):
  ...


@PARAM_SCHEDULERS.register_module()
class CustomMomentumScheduler(MomentumSchedulerMixin, CustomParameterScheduler):
  ...
