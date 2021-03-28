from enum import Enum
from net import Net
from schemes import *

class CMD_TYPE(Enum):
    None_ = 0
    Add = 1
    Ping = 2
    scheme = 3
    Exit = 4


class Command:
    def __init__(self):
        self.cmdType: CMD_TYPE = CMD_TYPE.None_

    def start(self, net: Net):
        pass


class AddCommand(Command):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.cmdType = CMD_TYPE.Add
        self.x = x
        self.y = y

    def start(self, net: Net):
        net.add_router(self.x, self.y)

class PingCommand(Command):
    def __init__(self, id_start_node: int, id_finish_node: int):
        super().__init__()
        self.cmdType = CMD_TYPE.Ping
        self.id_start = id_start_node
        self.id_finish = id_finish_node

    def start(self, net: Net):
        net.ping_routers(self.id_start, self.id_finish)

class schemeRing(Command):
    def __init__(self):
        super().__init__()
        self.cmdType = CMD_TYPE.scheme
        self.points = CreateRingScheme()

    def start(self, net: Net):
        for p_count in range(len(self.points)):
            net.add_router(self.points[p_count][0], self.points[p_count][1])


class schemeStar(Command):
    def __init__(self):
        super().__init__()
        self.cmdType = CMD_TYPE.scheme
        self.points = CreateStarScheme()


    def start(self, net: Net):
        for p_count in range(len(self.points)):
            net.add_router(self.points[p_count][0], self.points[p_count][1])


class schemeBus(Command):
    def __init__(self):
        super().__init__()
        self.cmdType = CMD_TYPE.scheme
        self.points = CreateBusScheme()

    def start(self, net: Net):
        for p_count in range(len(self.points)):
            net.add_router(self.points[p_count][0], self.points[p_count][1])

class schemeMesh(Command):
    def __init__(self):
        super().__init__()
        self.cmdType = CMD_TYPE.scheme
        self.points = CreateMeshScheme()

    def start(self, net: Net):
        for p_count in range(len(self.points)):
            net.add_router(self.points[p_count][0], self.points[p_count][1])


class ExitCommand(Command):
    def __init__(self):
        super().__init__()
        self.cmdType = CMD_TYPE.Exit