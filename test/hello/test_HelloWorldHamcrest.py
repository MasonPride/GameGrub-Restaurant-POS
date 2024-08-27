"""Test Class for HelloWorld using Hamcrest.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
from src.hello.HelloWorld import HelloWorld


class TestHelloWorldHamcrest():
    """Test Class for `src.hello.HelloWorld`."""

    def test_hello_world(self, capsys: CaptureFixture[Any]) -> None:
        """Test Method for `src.hello.HelloWorld.main`.

        This will test the main method with no arguments.

        Args:
            capsys: PyUnit fixture to capture output.
        """
        HelloWorld.main(["HelloWorld"])
        captured: CaptureResult[Any] = capsys.readouterr()
        assert_that(captured.out, is_("Hello World\n"), "Unexpected Output")

    def test_hello_world_arg(self, capsys: CaptureFixture[Any]) -> None:
        """Test Method for `src.hello.HelloWorld.main`.

        This will test the main method with 1 argument.

        Args:
            capsys: PyUnit fixture to capture output.
        """
        HelloWorld.main(["HelloWorld", "CC 410"])
        captured: CaptureResult[Any] = capsys.readouterr()
        assert_that(captured.out, is_("Hello CC 410\n"), "Unexpected Output")
