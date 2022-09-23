import random
from game_states.state_base import State, TerminalState, StateMachine


class A(State):

    def __init__(self):
        self.value = "A"
        transitions = {
            0: B,
            1: C
        }
        super().__init__(transitions=transitions)


class B(State):

    def __init__(self):
        self.value = "B"
        transitions = {
            0: C
        }
        super().__init__(transitions=transitions)


class C(State):

    def __init__(self):
        self.value = "C"
        transitions = {
            0: B,
            1: D
        }
        super().__init__(transitions=transitions)


class D(State):

    def __init__(self):
        self.value = "D"
        transitions = {
            0: B,
            1: C,
            2: F
        }
        super().__init__(transitions=transitions)


class F(TerminalState):

    def __init__(self):
        self.value = "F"
        super().__init__()


class TestMachine(StateMachine):

    def __init__(self, state: State):
        super().__init__(state=state)

