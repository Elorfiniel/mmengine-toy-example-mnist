# dataloader settings
train_dataloader = dict(
  dataset=dict(
    type='MNIST',
    root='data/mnist',
    train=True,
    transform=[
      dict(type='RandomRotation', degrees=20),
      dict(type='RandomResizedCrop', size=(28, 28), scale=(0.8, 1.0), ratio=(0.8, 1.25)),
      dict(type='ToTensor'),
    ],
    download=True,
  ),
  num_workers=4,
  batch_size=64,
  sampler=dict(
    type='DefaultSampler',
    shuffle=True,
  ),
  collate_fn=dict(type='default_collate'),
)

val_dataloader = dict(
  dataset=dict(
    type='MNIST',
    root='data/mnist',
    train=False,
    transform=[
      dict(type='ToTensor'),
    ],
    download=True,
  ),
  num_workers=4,
  batch_size=64,
  sampler=dict(
    type='DefaultSampler',
    shuffle=True,
  ),
  collate_fn=dict(type='default_collate'),
)

test_dataloader = val_dataloader

# evaluator settings
val_evaluator = dict(type='Accuracy')
test_evaluator = dict(type='Accuracy')
