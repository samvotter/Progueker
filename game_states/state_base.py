import typing


class State:
    """
    A State's single responsibility is to organize information relevant to that state.
    """

    def __init__(self, transitions: typing.Dict[typing.Any, typing.Any]):
        self.transitions = transitions

    def go_to_next_state(self, event: typing.Any):
        return self.transitions[event]()

    def __str__(self):
        return self.__class__.__name__


class TerminalState:
    """
    A TerminalState's single responsibility is to identify itself as a terminal point.
    """

    def __str__(self):
        return self.__class__.__name__


class StateMachine:
    """
    A StateMachine's single responsibility is traverse states.
    """

    def __init__(self, state: State):
        self.state = state

    def new_state(self, event: typing.Any):
        self.state = self.state.go_to_next_state(event)
