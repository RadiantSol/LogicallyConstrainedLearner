import math
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# generate the chosen track for the learner to train on
# here be curriculum learning

class World:
    def __init__(self, sim):
        self.sim = sim
        self.map = None
        self.scaler = MinMaxScaler((-5, 5))
 
    def generateTrack(self, trackNo):
        map = np.array([[' ' for _ in range(50)] for _ in range(50)])
        walls = []
        
        # straight line track, no traffic light
        if trackNo == 0:
            # generate 50x50 map
            walls = []
            for i in range(50):
                # generate off-road areas
                for j in range(15):
                    map[i][j] = 'o'
                    map[i][j+35] = 'o'
                # generate track portions
                map[i][20] = '|'
                map[i][25] = 'c'
                map[i][30] = '|'
                walls.append((i, 15))
                walls.append((i, 35))
            map[49][25] = 'g'
            goal = (49, 25)
            car = (0, 25)
        # straight line track, traffic light
        elif trackNo == 1:
            pass
        # curvy track, traffic light
        elif trackNo == 2:
            pass
        walls = self.scaler.fit_transform(walls)
        goal = self.scaler.transform([goal])
        car = self.scaler.transform([car])
        self.placeGoal(goal[0])
        self.placeWalls(walls)
        self.sim.setObjectPosition(self.sim.getObject('/Manta'), -1, [car[0][0], car[0][1], 1])
        pass

    def placeWalls(self, obs):
        shapeHandles = []
        for a, b in obs:
            shapeHandle = self.sim.createPrimitiveShape(self.sim.primitiveshape_cuboid, [0.25, 0.25, 1])
            self.sim.setObjectPosition(shapeHandle, -1, [a, b, 1])
            shapeHandles.append(shapeHandle)
        groupHandle=self.sim.groupShapes(shapeHandles, True)
        self.sim.setObjectAlias(groupHandle, 'Obstacle')
        
    def placeGoal(self, g):
        goal = self.sim.createPrimitiveShape(self.sim.primitiveshape_cuboid, [0.25, 0.25, 1])
        self.sim.setObjectPosition(goal, -1, [g[0], g[1], 1])
        self.sim.setShapeColor(goal, None, self.sim.colorcomponent_ambient, [0, 1, 0])
        self.sim.setObjectAlias(goal, 'Goal')