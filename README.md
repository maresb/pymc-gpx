# pymc-gpx

[![PyPI - Version](https://img.shields.io/pypi/v/pymc-experimental-manifold-gp.svg)](https://pypi.org/project/pymc-experimental-manifold-gp)

-----

Unstable and eXperimental manifold-oriented Gaussian processes for PyMC.

The goal is to sort out the API and eventually merge it into PyMC. We are mainly focused on HSGP, but may also tweak the normal GP implementation.

This API will break without notice, so it's strongly recommended to pin the exact version of this package.

## HSGP to-dos

- [ ] Add interval with Dirichlet boundary conditions
- [ ] Add interval with Neumann boundary conditions
- [ ] Add interval with Neumann boundary conditions and zero mean
- [ ] Add interval with periodic boundary conditions
- [ ] Add interval with mixed boundary conditions
- [ ] Add tensor products
- [ ] Add sphere
- [ ] Add disc with Dirichlet boundary conditions
- [ ] Add disc with Neumann boundary conditions
- [ ] Add harmonic oscillator

## Getting started

```bash
pip install pymc-gpx
```

```python
# Import the old but tweaked HSGP API
from gpx.old import HSGP
```

## Development

It's recommended to get and use [pixi](https://pixi.sh) and [pre-commit](https://pre-commit.com/). See the documentation for information on Pixi integration with IDEs like VS Code or JupyterLab.

```bash
# Enable pre-commit hooks
pre-commit install

# Run an activated shell
pixi shell

# Run mypy and tests
pixi run mypy
pixi run test
pixi run test-old
```
