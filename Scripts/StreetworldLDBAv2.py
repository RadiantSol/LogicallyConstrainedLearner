from src.automata.ldba import LDBA

StreetworldLDBA = LDBA(accepting_sets=[[1]])

def step(self, label) -> int:
    # state 0
    if self.automaton_state == 0:
        if 'goal' in label:
            if 'red' in label:
                self.automaton_state = -1
            else:
                self.automaton_state = 1
        elif 'road' in label:
            # if 'red' in label:
            #     if 'moving' in label:
            #         self.automaton_state = -1
            #     else:
            #         self.automaton_state = 0 
            # else:
                self.automaton_state = 0
        elif 'off' in label:
                self.automaton_state = -1
    # state 1
    elif self.automaton_state == 1:
        if 'off' in label:
            self.automaton_state = -1
        else:
            self.automaton_state = 1
    
    # state -1 (AKA BAD)
    elif self.automaton_state == -1:
        self.automaton_state = -1
    
    # step function returns the new automaton state
    return self.automaton_state

# override step function
LDBA.step = step.__get__(StreetworldLDBA, LDBA)