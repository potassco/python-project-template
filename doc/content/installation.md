# Installation

fillname requires Python 3.8+. We recommend version 3.10.

You can check a successful installation by running

```shell
fillname -h
```

## Installing with pip 


The python fillname package can be found [here](https://pypi.org/project/fillname/).

```shell
pip install fillname
```

## Development

### Installing from source

The project is hosted on [github](https://github.com/potassco/fillname) and can
also be installed from source.

```{warning}
We recommend this only for development purposes.
```

```{note}
The pip package `setuptools` must be previously installed
```

Execute the following command in the top level fillname directory:

```shell
git clone https://github.com/potassco/fillname
cd fillname
pip install -e .[all]
```
