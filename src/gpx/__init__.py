try:
    from gpx._version import __version__
except ImportError as e:
    raise RuntimeError(
        "Package 'gpx' is not correctly built or installed. "
        "If you are developing 'gpx', please reinstall it into your environment."
    ) from e

__all__ = ["__version__"]
