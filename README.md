# fillname

FILL-DESCRIPTION


## Installation

Requires Python 3.9

### Local dev mode using pip

```shell 
pip install -e .[dev]
```

### Conda

Install dependencies with [conda](https://anaconda.org) based on the [environment.yml](environment.yml) file.

```shell
conda env create -f environment.yml
```

```shell
conda env create -f environment.yml
```



### Manual installation
<!-- Install submodules

```shell
$ git submodule update --init --recursive
``` -->

<!-- Install [clingo](https://potassco.org/doc/start/) preferably using `conda`.
We use version `5.4.0`

```shell
$ conda install -c potassco clingo
``` -->

### Tests

Run tests using `pytest`

```shell
$ pytest -v tests/test.py
```

Add flag `-s` to show print statements in the code