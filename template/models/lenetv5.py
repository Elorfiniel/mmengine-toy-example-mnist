from mmengine.model import BaseModel

from template.registry import MODELS


@MODELS.register_module()
class LeNetv5(BaseModel):
  ...
