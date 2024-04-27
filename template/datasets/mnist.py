from mmengine.dataset import BaseDataset

from template.registry import DATASETS


@DATASETS.register_module()
class CustomMNIST(BaseDataset):
  ...
