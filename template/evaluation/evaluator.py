from mmengine.evaluator import Evaluator

from template.registry import EVALUATOR


@EVALUATOR.register_module()
class CustomEvaluator(Evaluator):
  ...
