def move_target(sim, action):
        #get location of current robot
        car = sim.getObject('/PioneerP3DX')

        dx = 1/10
        dy = 1/10

        #car absolute position
        carx, cary, carz = sim.getObjectPosition(car, -1)

        x = int(carx/dx)
        y = int(cary/dy)

        #get target handle
        car = sim.getObject('/PioneerP3DX/Target')

        #move target to location given 
        if action == 0: #north
            #+1 x, +0 y
            pass
        elif action == 1: #north_east
            #+1 x, +1 y
            pass
        elif action == 2: #east
            #+0 x, +1 y
            pass
        elif action == 3: #south_east
            #-1 x, +1 y
            pass
        elif action == 4: #south
            #-1 x, +0 y
            pass
        elif action == 5: #south_west
            #-1 x, -1 y
            pass
        elif action == 6: #west
            #-1 x, 0 y
            pass
        elif action == 7: #north_west
            #+1 x, -1 y
            pass
        elif action == 8: #stay
            #0x, 0y
            pass