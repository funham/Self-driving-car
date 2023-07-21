import time


class Timer:
    def __init__(self, duration: float = 0):
        self.set(duration)

    def is_expired(self):
        return time.monotonic() - self._start_time >= self.duration

    def progress(self) -> float:
        return (time.monotonic() - self._start_time) / self.duration

    def set(self, duration):
        self.duration = duration
        self._start_time = time.monotonic()
