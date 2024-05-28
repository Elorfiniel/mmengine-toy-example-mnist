from mmengine.evaluator import BaseMetric

from template.registry import METRICS


@METRICS.register_module()
class CustomMetric(BaseMetric):
  ...


@METRICS.register_module()
class Accuracy(BaseMetric):
  def process(self, data_batch, data_samples):
    preds, labels = data_samples
    self.results.append(dict(
      n_total=len(labels),
      n_correct=(preds == labels).sum().cpu(),
    ))

  def compute_metrics(self, results):
    n_total = sum([x['n_total'] for x in results])
    n_correct = sum([x['n_correct'] for x in results])

    return dict(accuracy=100 * n_correct / n_total)
