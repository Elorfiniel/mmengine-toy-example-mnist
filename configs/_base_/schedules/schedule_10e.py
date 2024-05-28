# optimizer settings
optimizer = dict(
  type='SGD',
  lr=0.01,
  momentum=0.95,
  weight_decay=0.005,
)
optim_wrapper = dict(type='OptimWrapper', optimizer=optimizer)

# scheduler settings
param_scheduler = dict(
  type='MultiStepLR',
  milestones=[6, 8],
  gamma=0.5,
  by_epoch=True,
  verbose=True,
)

# runner schedule settings
train_cfg = dict(by_epoch=True, max_epochs=10, val_begin=2, val_interval=1)
val_cfg = dict()
test_cfg = dict()

# default hooks
default_hooks = dict(
  timer=dict(type='IterTimerHook'),
  logger=dict(type='LoggerHook', interval=50, log_metric_by_epoch=False),
  param_scheduler=dict(type='ParamSchedulerHook'),
  checkpoint=dict(type='CheckpointHook', interval=1, by_epoch=True, max_keep_ckpts=4),
)

custom_hooks = [
  dict(
    type='CheckpointHook',
    interval=1,
    by_epoch=True,
    # metric name specified in `compute_metrics`
    save_best='accuracy',
    rule='greater',
    save_begin=2,
  ),
]
