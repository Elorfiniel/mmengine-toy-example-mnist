from .base import BaseTransform

from template.registry import TRANSFORMS


@TRANSFORMS.register_module()
class CustomTransform(BaseTransform):
  ...
