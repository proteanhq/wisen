# wisen

`wisen` is a Python library designed to ensure and validate schema evolution over time. It provides tools for checking forward and backward compatibility of data schemas and is built to support various data encoding and schema standards, including JSON Schema, Apache Avro, Google's Protocol Buffers (Protobuf), and Apache Thrift.

> :warning: **Warning**: `wisen` is currently in active development and is not ready for production use. The API is unstable and subject to change. We welcome feedback and contributions, but please use it at your own risk.

## Features

- **Schema Compatibility Checks**: Validate that a new version of a schema is backward or forward compatible with an older version.
- **Schema Version Management**: Manage schema versions and provide a registry for schema retrieval.
- **Support for Multiple Encoding Schemes**: Abstract interfaces for different encoding schemes allowing for extensibility and custom implementations.
- **Detailed Error Reporting**: Get comprehensive error reports about schema incompatibilities.
- **CLI and Library Interface**: Use `wisen` as a command-line tool or as a library in your Python projects.
- **CI/CD Integration**: Easily integrate `wisen` into your continuous integration and deployment workflows.
- **Flexible Logging**: Configure logging to suit different environments, from development to production.

## Installation

To install `wisen`, simply use `poetry` or `pip`:

```sh
poetry add wisen
```

Or

```sh
pip install wisen
```

## Quickstart

Here's a quick example to get you started:

```python
from wisen import SchemaCompatibilityChecker

checker = SchemaCompatibilityChecker()

# Check if the new schema is backward compatible with the old schema
compatible = checker.is_compatible(new_schema, old_schema, 'backward')

print(f"The schemas are {'compatible' if compatible else 'incompatible'}.")
```

For command-line usage:

```sh
wisen check --new-schema path/to/new/schema.json --old-schema path/to/old/schema.json --type backward
```

## Documentation

For more detailed usage and a full list of features, please refer to the [documentation](#).

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow the [contributing guidelines](CONTRIBUTING.md).

## License

`wisen` is released under the MIT License. See [LICENSE](LICENSE) for details.
