import selenium
import pytest
import importlib.metadata as metadata

print("SELENIUM VERSION:", selenium.__version__)
print("PYTEST VERSION:", pytest.__version__)

# safer way to check pytest-html version
print("PYTEST-HTML VERSION:", metadata.version("pytest-html"))