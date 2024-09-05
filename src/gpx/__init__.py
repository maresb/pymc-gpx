from importlib.metadata import version

# Warning: this is the version as of the last build or install,
# so it might not be up-to-date during development.
__version__ = version("pymc-gpx")

__all__ = ["__version__"]
