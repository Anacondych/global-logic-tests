import subprocess
import pytest

from configuration import PORT, HOST


@pytest.fixture(autouse=True)
def start_server():
    """Fixture to start server in background."""
    subprocess.run(["iperf3", "-s",
                    "-p", PORT,
                    "--daemon"])


@pytest.fixture
def start_client():
    def _inner(*args):
        """Fixture to start client sending transmission."""
        subprocess.run(["iperf3",
                        "-c", HOST, "-p", PORT,
                        *args])
    return _inner
