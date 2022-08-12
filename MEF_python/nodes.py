class State:
    """
    This is a second possible implementation of a Finite Machine State
    """

    def __init__(self, result):
        self.result = result
        self.params = {}

    def add_state(self, input, state):
        self.params[input] = state
    
    def next_state(self, input):
        if input == "":
            return self.get_result()
        return self.params[input[0]].next_state(input[1:])

    def get_result(self):
        return self.result

if __name__ == "__main__":
    start = State(False)
    s0 = State(False)
    s1 = State(False)
    s2 = State(True)
    s3 = State(True)
    s4 = State(False)

    start.add_state("a", s0)
    start.add_state("b", s3)
    s0.add_state("a", s4)
    s0.add_state("b", s1)
    s1.add_state("a", s4)
    s1.add_state("b", s2)
    s2.add_state("a", s0)
    s2.add_state("b", s2)
    s3.add_state("a", s0)
    s3.add_state("b", s3)
    s4.add_state("a", s4)
    s4.add_state("b", s4)

    print(start.next_state(input="bbbb"))
