#python
import random

def changeLightColor(color, sim):
    if color == 'red':
        sim.setShapeColor(sim.getObject('/Light'), None, sim.colorcomponent_ambient, [1, 0, 0])
    elif color == 'green':
        sim.setShapeColor(sim.getObject('/Light'), None, sim.colorcomponent_ambient, [0, 1, 0])
    elif color == 'yellow':
        sim.setShapeColor(sim.getObject('/Light'), None, sim.colorcomponent_ambient, [1, 1, 0])
        
def non_sync(sim):
    # e.g. non-synchronized loop:
    sim.setThreadAutomaticSwitch(False)
    light = 'red'
    changeLightColor(light, sim)
    
    while True:
        greenLight = random.choice([True, False])
        # green light condition
        if greenLight:
            if light == 'red':
                light = 'green'
                changeLightColor(light, sim)
        # red light condition
        else:
            # if light is green, change to yellow, wait some time, then to red
            if light == 'green':
                light = 'yellow'
                changeLightColor(light, sim)
                sim.setStringSignal('TrafficLight', 'yellow')
                sim.wait(2) # this could be a hyperparameter?
                light = 'red'
                changeLightColor(light, sim)
        # wait 1 second before each light change evaluation
        sim.setStringSignal('TrafficLight', light)
        sim.wait(1)

# See the user manual or the available code snippets for additional callback functions and details
