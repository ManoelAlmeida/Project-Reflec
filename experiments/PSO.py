from __future__ import division
import random
import math
from Particle import Particle

class PSO():
    def __init__(self,func_fitness,x0,bounds,num_particles,maxiter):

        err_best_g=-1                   # best error for group
        pos_best_g=[]                   # best position for group

        # establish the swarm
        swarm=[]
        for i in range(0,num_particles):
            swarm.append(Particle(x0))

        # begin optimization loop
        i=0
        while i < maxiter:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,num_particles):
                swarm[j].evaluate(func_fitness)

                # determine if current particle is the best (globally)
                if swarm[j].err < err_best_g or err_best_g == -1:
                    pos_best_g=list(swarm[j].position)
                    err_best_g=float(swarm[j].err)

            # cycle through swarm and update velocities and position
            for j in range(0,num_particles):
                swarm[j].update_velocity_intertia(pos_best_g)
                #swarm[j].update_velocity_clerc(pos_best_g)
                swarm[j].update_position(bounds)
            i+=1

        # print final results
        print('Best position: ', pos_best_g)
        print('Best error: ', err_best_g)

