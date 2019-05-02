# cylc-jinja2filters

Jinja2 filters for Cylc. These are loaded automatically via setuptools.
Users are expected to use `cylc.jinja2filters.filters` to put the filters
under this package into the Jinja2 `filters` filters scope. Ditto for
`cylc.jinja2filters.globals` and `cylc.jinja2filters.tests`.

## Building

```bash
# For a complete install
$ pip install .

# For an editable install
$ pip install -e .
```
