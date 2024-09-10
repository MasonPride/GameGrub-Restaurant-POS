"""Test Class for HelloWorld.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
from pytest import CaptureFixture
from _pytest.capture import CaptureResult
from typing import Any
from src.hello.HelloWorld import HelloWorld


class TestHelloWorld():
    """Test class for 'srs.hello.HelloWorld.py'."""

    def test_hello_world(self, capsys: CaptureFixture[Any]) -> None:
        """Test Method for `src.hello.HelloWorld.main`.

        This will test the main method with no arguments.

        Args:
            capsys: PyUnit fixture to capture output.
        """
        HelloWorld.main(["HelloWorld"])
        captured: CaptureResult[Any] = capsys.readouterr()
        assert captured.out == "Hello World\n", "Unexpected Output"

    def test_hello_world_arg(self, capsys):
        """Test Method for `src.hello.HelloWorld.main`.

        This will test the main method with 1 argument.

        Args:
            capsys: PyUnit fixture to capture output.
        """
        HelloWorld.main(["HelloWorld", "CC 410"])
        captured = capsys.readouterr()
        assert captured.out == "Hello CC 410\n", "Unexpected Output"

