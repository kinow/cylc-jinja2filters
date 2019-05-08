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

## Example suite

```bash
#!Jinja2

[cylc]
    UTC mode = True

[scheduling]
    initial cycle point = 01231212T1212
    [[dependencies]]
        [[[R1]]]
            graph = reverse_upper
[runtime]
    [[reverse_upper]]
        script = """test "$TEST_1" == 'OLUAP OAS'"""
        [[[environment]]]
            TEST_1 = {{ 'sao paulo' | reverse_upper }}

```