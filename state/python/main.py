from __future__ import annotations
from abc import ABC, abstractmethod
from time import time


class FailsafeSocket:
    def __init__(self) -> None:
        self.queue = []
        self.states = {
            "offline": Offline(self),
            "online": Online(self),
            "pending": Pending(self),
        }
        self.change_state("offline")

    def change_state(self, state):
        self.state = self.states[state]

    def send(self, data):
        self.state.send(data)


class AbstractState(ABC):
    @abstractmethod
    def send(self) -> None:
        pass


class Offline(AbstractState):
    def __init__(self, FailsafeSocket):
        self.socket = FailsafeSocket

    def send(self, data) -> None:
        print(f"{type(self).__name__} {data} not sent ")


class Pending(AbstractState):
    def __init__(self, FailsafeSocket):
        self.socket = FailsafeSocket

    def send(self, data) -> None:
        self.socket.queue.append(data)
        print(f"{type(self).__name__} data {data} added to queue: {self.socket.queue}")


class Online(AbstractState):
    def __init__(self, FailsafeSocket):
        self.socket = FailsafeSocket

    def send(self, data) -> None:
        if len(data) > 5:
            self.socket.change_state("offline")
            print(f"{type(self).__name__} too long data {data}, change to noline")
            self.socket.queue = []
        else:
            self.socket.queue.append(data)
            print(f"{type(self).__name__} sent data: {self.socket.queue}")
            self.socket.queue = []


# 상태가 ON/OFF 일때 context의 send에서 분기가 있는 것이 아니라 해당 상태 객체에 정의된 메서드에 의해 할일을 수행
# 상태가 여러개라고 가저한다면 if 선언문을 제거할수 있고
# 상태의 변경에는 닫혀있지만 상태 확장에는 열려있음


if __name__ == "__main__":
    socket = FailsafeSocket()
    socket.send("1")
    socket.send("2")
    socket.send("3")
    socket.change_state("pending")
    socket.send("4")
    socket.send("5")
    socket.send("6")
    socket.change_state("online")
    socket.send("7")
    socket.send("8")
    socket.send("9")
    socket.send("11111111")
    socket.send("1")

    # socket1 = FailsafeSocket()
    # socket1.send("1")
    # socket1.send("2")
    # socket1.send("3")
    # socket1.change_state("pending")
    # socket1.send("4")
    # socket1.send("5")
    # socket1.send("6")
    # socket1.change_state("online")
    # socket1.send("7")
    # socket1.send("8")
    # socket1.send("9")

    # print(socket1 == socket)  # false
    # print(socket.state.socket == socket1.state.socket)  # false
