import loguru
import pytest


@pytest.fixture(autouse=True)
def reset_logger():
    def reset():
        loguru.logger.remove()
        loguru.logger.__init__(loguru._logger.Core(), None, 0, False, False, False, False, True, None, {})
        loguru._logger.context.set({})

    reset()
    yield
    reset()


@pytest.fixture
def writer():
    def w(message):
        w.written.append(message)

    w.written = []
    w.read = lambda: "".join(w.written)
    w.clear = lambda: w.written.clear()

    return w
