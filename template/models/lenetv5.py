from mmengine.model import BaseModel

from template.registry import MODELS

import torch as torch
import torch.nn as nn


@MODELS.register_module()
class LeNetv5(BaseModel):
  '''Implementation of LeNet-v5 with modifications:

  1) Sigmoid activation is replaced with ReLU activaiton.
  2) Average pooling is replaced with max pooling.
  3) The number of neurons in the 2nd FC layer is reduced (84 -> 64).

  Both input shape and output shape are in the (N, C, H, W) format.

  This implementation targets MNIST dataset published by LeCun:

    http://yann.lecun.com/exdb/mnist/'''

  def __init__(self, in_channels=1, n_classes=10):
    super(LeNetv5, self).__init__()
    self.backbone = nn.Sequential(
      nn.Conv2d(in_channels, 6, kernel_size=5, stride=1, padding=2),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2, stride=2, padding=0),
      nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=0),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2, stride=2, padding=0),
      nn.Flatten(),
      nn.Linear(16*5*5, 120),
      nn.ReLU(),
      nn.Linear(120, 64),
      nn.ReLU(),
      nn.Linear(64, n_classes),
    )

  def forward(self, images, labels, mode='tensor'):
    feats = self.backbone(images)

    if mode == 'loss':
      loss = nn.functional.cross_entropy(feats, labels)
      return dict(loss=loss)

    if mode == 'predict':
      preds = torch.argmax(feats, dim=1)
      return preds, labels

    return feats
