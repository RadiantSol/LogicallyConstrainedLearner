from src.automata.ldba import LDBA

StreetworldLDBA = LDBA(accepting_sets=[[1]])

def step(self, label) -> int:
    # state 0
    if self.automaton_state == 0:
        if 'goal' in label:
            self.automaton_state = 1
        elif 'road' in label:
                self.automaton_state = 0
        elif 'off' in label:
                self.automaton_state = -1
    # state 1
    if self.automaton_state == 1:
        self.automaton_state = 1
    
    # state -1 (AKA BAD)
    if self.automaton_state == -1:
        self.automaton_state = -1

    # step function returns the new automaton state
    return self.automaton_state

# override step function
LDBA.step = step.__get__(StreetworldLDBA, LDBA)