#python

#python
import math
import numpy as np 

L = 0.381
R = 0.195 / 2

def uni_to_diff(v, w):
    vR = (2 * v + w * L) / ( 2 * R)
    vL = (2 * v - w * L) / ( 2 * R)
    return vR, vL

def non_sync(sim):
    # e.g. non-synchronized loop:
    sim.setThreadAutomaticSwitch(True)
    motorLeft=sim.getObject("./leftMotor")
    motorRight=sim.getObject("./rightMotor")
    #goal = sim.getObject("/Target")
    robot = sim.getObject(".")
    goal = sim.getObject("./Target")
    sim.setObjectParent(goal,-1,True)
    
    obstacles=sim.createCollection(0)
    sim.addItemToCollection(obstacles,sim.handle_all,-1,0)
    sim.addItemToCollection(obstacles,sim.handle_tree,robot,1)
    usensors={}
    for i in range(16):
        usensors[i]=sim.getObject("./ultrasonicSensor["+str(i)+"]")
        sim.setObjectInt32Param(usensors[i],sim.proxintparam_entity_to_detect,obstacles)
    noDetectionDist=0.5
    maxDetectionDist=0.3
    detect=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    braitenbergL=[-0.2,-0.4,-0.6,-0.8,-1,-1.2,-1.4,-1.6, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    braitenbergR=[-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,-0.2, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    v0=2
    
    Kp = .25
    Kalpha = .35
    
    while True:
        GTR = np.array(sim.getObjectPosition(goal, robot))

        
        # position error 
        err = np.linalg.norm(GTR)
        
        # acceptable goal region
        if err < L :
            err = 0

        vR, vL = 0, 0    
        
        if err > 0:
            print(f"position error = {err:.3f}")
            vR, vL = uni_to_diff(Kp * GTR[0],  Kalpha* GTR[1])
        
        #avoid dynamic obstacles
        for i in range(16):
            res,dist,_,_,_=sim.readProximitySensor(usensors[i])
            if (res>0) and (dist<noDetectionDist):
                if (dist<maxDetectionDist):
                    dist=maxDetectionDist
                detect[i]=1-((dist-maxDetectionDist)/(noDetectionDist-maxDetectionDist))
            else:
                detect[i]=0
        for i in range(16):
            vL=vL+braitenbergL[i]*detect[i]
            vR=vR+braitenbergR[i]*detect[i]
        
        sim.wait(1)
        sim.setJointTargetVelocity(motorLeft, vL)
        sim.setJointTargetVelocity(motorRight, vR)