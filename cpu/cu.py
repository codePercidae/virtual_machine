from cpu.alu import Alu
from cpu.register import Register

class CU:

    def __init__(self) -> None:
        self.alu = Alu()
        self.ir = Register()
        self.sr = Register()
        self.tr = Register()
        self.pc = Register()
        self.r1 = Register()
        self.r2 = Register()
        self.r3 = Register()
        self.r4 = Register()
        self.r5 = Register()
        self.r6 = Register()
        self.r7 = Register()

    def decode(self):
        pass

    def clock(self):
        pass