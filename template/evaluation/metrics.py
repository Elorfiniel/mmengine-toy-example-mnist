from mmengine.evaluator import BaseMetric

from template.registry import METRICS


@METRICS.register_module()
class CustomMetric(BaseMetric):
  ...
