def move_target(sim, action, car, target_handle):
        #get location of current robot
        #car = sim.getObject('/PioneerP3DX')

        dx = 1
        dy = 1

        #car absolute position
        carx, cary, carz = sim.getObjectPosition(car, sim.handle_world)

        x = int(carx/dx)
        y = int(cary/dy)

        #get target handle
        #target_handle = sim.getObject('/Target')

        
        #move target to location given 
        if action == 0: #north
            #+1 x, +0 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx+dx, cary, carz])
        elif action == 1: #north_east
            #+1 x, +1 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx+dx, cary+dy, carz])
        elif action == 2: #east
            #+0 x, +1 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx, cary+dy, carz])
        elif action == 3: #south_east
            #-1 x, +1 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx-dx, cary+dy, carz])
        elif action == 4: #south
            #-1 x, +0 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx-dx, cary, carz])
        elif action == 5: #south_west
            #-1 x, -1 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx-dx, cary-dy, carz])
        elif action == 6: #west
            #-1 x, 0 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx-dx, cary, carz])
        elif action == 7: #north_west
            #+1 x, -1 y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx+dx, cary-dy, carz])
        elif action == 8: #stay
            #0x, 0y
            sim.setObjectPosition(target_handle, sim.handle_world, [carx, cary, carz])
            