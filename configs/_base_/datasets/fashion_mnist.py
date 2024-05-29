# Inherent from configs for MNIST dataset
_base_ = ['./mnist.py']

# dataloader settings
train_dataloader = dict(
  dataset=dict(
    type='FashionMNIST',
    root='data/fashion_mnist',
  ),
)

val_dataloader = dict(
  dataset=dict(
    type='FashionMNIST',
    root='data/fashion_mnist',
  ),
)

test_dataloader = val_dataloader
