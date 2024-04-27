from mmengine.hooks import Hook

from template.registry import HOOKS


@HOOKS.register_module()
class CustomHook(Hook):
  priority = 'NORMAL'

  ...
