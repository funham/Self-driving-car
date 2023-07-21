import time


class Ticker:
    _t0: float = time.monotonic()
    _dt: float = time.monotonic()

    @staticmethod
    def update() -> float:
        t1 = time.monotonic()
        Ticker._dt = t1 - Ticker._t0
        Ticker._t0 = t1

        return Ticker._dt

    @property
    def dt(self) -> float:
        return self._dt

    @property
    def fps(self) -> float:
        return 1 / self._dt
