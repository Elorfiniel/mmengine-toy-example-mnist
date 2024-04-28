from mmengine.dataset import Compose

from template.registry import DATASETS

import torchvision as tv


def compose_multiple_transform(transform):
  if isinstance(transform, dict):
    transform = [transform]
  if isinstance(transform, (list, tuple)):
    transform = Compose(transform)

  return transform


@DATASETS.register_module(name='MNIST', force=False)
def build_torchvision_mnist(transform=None, **kwargs):
  transform = compose_multiple_transform(transform)
  return tv.datasets.MNIST(**kwargs, transform=transform)


@DATASETS.register_module(name='FashionMNIST', force=False)
def build_torchvision_fashion_mnist(transform=None, **kwargs):
  transform = compose_multiple_transform(transform)
  return tv.datasets.FashionMNIST(**kwargs, transform)
