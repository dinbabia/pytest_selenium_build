import pytest

@pytest.mark.usefixtures("initialize")
class BaseTest:
    print("\nStarting point.")
    pass