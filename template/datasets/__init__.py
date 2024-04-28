from .mnist import CustomMNIST
from .fashion_mnist import CustomFashionMNIST
from .torchvision import (
  build_torchvision_mnist, build_torchvision_fashion_mnist,
)

__all__ = [
  'CustomMNIST', 'CustomFashionMNIST',
  'build_torchvision_mnist',
  'build_torchvision_fashion_mnist',
]
