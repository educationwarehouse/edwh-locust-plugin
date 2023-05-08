# edwh-demo-plugin

[![PyPI - Version](https://img.shields.io/pypi/v/edwh-demo-plugin.svg)](https://pypi.org/project/edwh-demo-plugin)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edwh-demo-plugin.svg)](https://pypi.org/project/edwh-demo-plugin)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## USING THIS TEMPLATE REPOSITORY
1. remove this markdown section;
2. replace 'demo' in README.md, pyproject.toml and the name of the plugin in `src` to your actual plugin name;
3. (add your actual plugin code of course);
4. run `semantic-release publish`, `hatch build -c` and `hatch publish`.

## Installation

```console
pip install edwh-demo-plugin
```

But probably you want to install the whole edwh package:

```console
pipx install edwh[demo]
# or
pipx install edwh[plugins,omgeving]
```

## License

`edwh-demo-plugin` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
