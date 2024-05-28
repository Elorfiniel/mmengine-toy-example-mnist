from mmengine.model import BaseModel

from template.registry import MODELS

import torch as torch
import torch.nn as nn


@MODELS.register_module()
class DummyMLP(BaseModel):
  '''Implementation of a dummy multi-layer perceptron.

  Both input shape and output shape are in the (N, C, H, W) format.

  This implementation targets MNIST dataset published by LeCun:

    http://yann.lecun.com/exdb/mnist/
  '''

  def __init__(self, in_channels=1, n_classes=10):
    super(DummyMLP, self).__init__()
    self.backbone = nn.Sequential(
      nn.Flatten(),
      nn.Linear(in_channels * 28 * 28, 128),
      nn.LeakyReLU(negative_slope=0.001),
      nn.Linear(128, 128),
      nn.LeakyReLU(negative_slope=0.001),
      nn.Linear(128, 64),
      nn.LeakyReLU(negative_slope=0.001),
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
