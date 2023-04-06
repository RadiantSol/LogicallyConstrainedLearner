from src.automata.ldba import LDBA

StreetworldLDBA = LDBA(accepting_sets=[[1], [2], [3]])

def step(self, label):
    # state 0
    if self.automaton_state == 0:
        if 'goal' in label:
            self.automaton_state = 1
        else:
            self.automaton_state = 0
    # state 1
    elif self.automaton_state == 1:
        self.automaton_state = 1

    # step function returns the new automaton state
    return self.automaton_state

# override step function
LDBA.step = step.__get__(StreetworldLDBA, LDBA)