# This question is asked by Google.

# Create a class CallCounter that tracks the number of calls a client has made within the last 3 seconds.
# Your class should contain one method, ping (int t) that receives the current
# timestamp (in milliseconds) of a new call being made and returns the number of calls made within the last 3 seconds.
#
# Note: you may assume that the time associated with each subsequent call to ping is strictly increasing.

# Ex: Given the following calls to ping…

# ping(1), return 1 (1 call within the last 3 seconds)
# ping(300), return 2 (2 calls within the last 3 seconds)
# ping(3000), return 3 (3 calls within the last 3 seconds)
# ping(3002), return 3 (3 calls within the last 3 seconds)
# ping(7000), return 1 (1 call within the last 3 seconds)

from typing import List
import unittest


class CallCounter:
    INTERVAL: int = 3000

    def __init__(self) -> None:
        self.pings: List[int] = []

    def ping(self, ping: int) -> str:
        self.__append_ping(ping)

        return self.__recent_pings(ping)

    def __append_ping(self, ping: int) -> None:
        self.pings.append(ping)

    def __recent_pings(self, ping: int) -> int:
        period: int = ping - self.INTERVAL
        index: int = 0
        period_start_ping: int = self.pings[index]

        while period_start_ping < period:
            index += 1
            period_start_ping = self.pings[index]

        return len(self.pings[index:])


class CallCounter2:
    INTERVAL: int = 3000

    def __init__(self) -> None:
        self.pings: List[int] = []

    def ping(self, timestamp: int) -> str:
        self.__append_ping(timestamp)

        period_start = self.__calculate_period_start(timestamp)
        self.__dequeue_pings(period_start)

        return self.__size()

    def __append_ping(self, ping: int) -> None:
        self.pings.append(ping)

    def __calculate_period_start(self, timestamp: int) -> int:
        return timestamp - self.INTERVAL

    def __dequeue_pings(self, period_start) -> None:
        if len(self.pings) < 1:
            return

        ping: int = self.pings[0]

        while ping < period_start:
            self.pings.pop(0)
            ping = self.pings[0]

    def __size(self) -> int:
        return len(self.pings)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.counter = CallCounter()
        self.counter2 = CallCounter2()

    def test_1(self):
        self.assertEqual(self.counter.ping(1), 1)
        self.assertEqual(self.counter.ping(300), 2)
        self.assertEqual(self.counter.ping(3000), 3)
        self.assertEqual(self.counter.ping(3002), 3)
        self.assertEqual(self.counter.ping(7000), 1)

    def test_2(self):
        self.assertEqual(self.counter2.ping(1), 1)
        self.assertEqual(self.counter2.ping(300), 2)
        self.assertEqual(self.counter2.ping(3000), 3)
        self.assertEqual(self.counter2.ping(3002), 3)
        self.assertEqual(self.counter2.ping(7000), 1)


if __name__ == "__main__":
    unittest.main()
