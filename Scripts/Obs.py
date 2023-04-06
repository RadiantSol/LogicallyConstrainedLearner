from math import atan2, pi
class Observation:
    def __init__(self, x, y, z, theta, delta_x, delta_y, delta_theta, velocity) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta
        self.dx = delta_x
        self.dy = delta_y
        self.dt = delta_theta
        self.velocity = velocity
        pass

    def get_vector(self) -> list:
        vec = list()
        vec.append(int(self.x / self.dx))
        vec.append(int(self.y / self.dy))
        vec.append(int(self.z ))
        vec.append(int(self.theta / self.dt))
        vec.append(int(self.velocity))
        return vec

    def check_goal(sim):
        car = sim.getObject('/Manta')
        goal = sim.getObject('/Goal')
        x, y, z = sim.getObjectPosition(car, goal)
        if (x < 1) and (y < 1):
            return True
        else:
            return False

    def get_observation(sim):
            car = sim.getObject('/Manta')
            goal = sim.getObject('/Goal')
            # get position of car
            x, y, z = sim.getObjectPosition(car, goal)

            dx = 1/10
            dy = 1/10
            
            #TO-DO get yaw from Quaternion
            x,y,z,w =sim.getObjectQuaternion(car, goal)
            yaw = atan2(2.0*(w * z + x * y), (w * w + x * x - y * y - z * z))
            dt = 1/(2*pi)
            
            # get velocity of car
            car_script = sim.getScript(sim.scripttype_childscript, car)
            velocity = sim.callScriptFunction('getSpeed', car_script)
            obs = Observation(x,y,z,yaw,dx,dy,dt,velocity)
            return 1