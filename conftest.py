import subprocess
import pytest

from configuration import PORT, HOST
from enums.iperf_enums import IperfErrorMessages


@pytest.fixture(autouse=True, scope='session')
def start_server():
    """Fixture to start server in background."""
    server = subprocess.Popen(["iperf3", "-s",
                               "-p", PORT])
    poll = server.poll()
    if poll is None:
        yield
        server.terminate()
    else:
        raise Exception(IperfErrorMessages.SERVER_NOT_LAUNCHED.value)


@pytest.fixture
def start_client():
    def _inner(*args):
        """Fixture to start client sending transmission."""
        client = subprocess.run(["iperf3",
                                 "-c", HOST, "-p", PORT,
                                 *args])
        if client.returncode != 0:
            raise Exception(IperfErrorMessages.CLIENT_NOT_LAUNCHED.value)

    return _inner
