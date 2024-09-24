# MMEngine Toy Example (MNIST)

This project demonstrates the basic usage of `mmengine`. By training a classification network on [MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database), this repository shows how deep learning problems are elegantly solved with the **Config & Registry** mechanism in `mmengine`.

This project follows the design pattern and philosophy of these official repositories by [OpenMMLab](https://openmmlab.com/):

1. [mmengine-template](https://github.com/open-mmlab/mmengine-template)
2. [mmsegmentation](https://github.com/open-mmlab/mmsegmentation)

Best regards to the OpenMMLab team, for such an amazing framework. 🤗🤗🤗

## Setup

To train or test the model, please follow these steps:

1. Install the requirements for the project.
2. Set `PYTHONPATH` properly.
3. Start training or testing with scripts in the toolset.

The following cheatsheet demonstrates how you can properly configure runtime environment for scripts in the `tools` folder. Feel free to follow the examples provided, but remember, your mileage may vary. Adapt the code and methods to suit your own habits and preferences!

### Install Dependencies

```shell
# create a python virtual environment for dependencies
python -m venv --upgrade-deps venv

# activate the virtual environment
venv/Scripts/Activate.ps1 # (windows: pwsh)
source venv/bin/activate  # (linux / mac)

# install required dependencies using pip
pip install -r requirements.txt
```

### Configure Python Module Search Path

Before the execution of scripts in the toolset, you need to make sure the Python interpreter knows where to find the `template` module (consists of files in the `template` folder). The cheatsheet achives this by setting the `PYTHONPATH` enrironment variable in each shell that executes the scripts.

`PYTHONPATH` is an environment variable used by Python to specify additional directories where the Python interpreter should look for modules and packages. When you execute a Python script, paths specified are appended in `sys.path`, which usually contains, in order, the directory of the script, directories listed in the `PYTHONPATH` variable, and the default directories where Python's standard library modules and third-party library modules are installed.

```shell
$ENV:PYTHONPATH = /path/to/template/folder  # (windows: pwsh)
export PYTHONPATH=/path/to/template/folder  # (linux / mac)
```

### Run Scripts for Training or Testing

For more information on how to invoke these scripts, please refer to [mmengine documents](https://mmengine.readthedocs.io/zh-cn/latest/advanced_tutorials/config.html).

```shell
# run example training script for classifier on the mnist dataset
python tools/train.py --work-dir runs/mnist-train configs/lenetv5/lenetv5-mnist-10e-28x28.py

# run example training script for classifier on the fashion mnist dataset
python tools/train.py --work-dir runs/mnist-train configs/lenetv5/lenetv5-fashion_mnist-10e-28x28.py
```

## Try with Trained Models

```shell
# run test using trained parameters on mnist dataset
python tools/test.py --work-dir runs/mnist-test configs/lenetv5/lenetv5-mnist-10e-28x28.py checkpoints/lenetv5-mnist-best-acc.pth

# run test using trained parameters on fashion dataset
python tools/test.py --work-dir runs/mnist-test configs/lenetv5/lenetv5-fashion_mnist-10e-28x28.py checkpoints/lenetv5-fashion_mnist-best-acc.pth
```

## Reference

For detailed guides on how you can customize the project to your own needs (custom datasets, runtime hooks, new metrics, etc), have a look at the documentation in [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) and [mmdetection](https://github.com/open-mmlab/mmdetection). The `user_guides` and `advanced_guides` sections under the `doc` folder are valuable resource you need.
