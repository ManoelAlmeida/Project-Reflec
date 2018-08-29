from __future__ import division
import random
import math
import time
from Particle import Particle

class PSO():
    def __init__(self,func_fitness, dimensions, num_particles, max_iterations):
        self.convergence_time = -1
        self.best_position = []
        self.best_error = -1
        self.error_history = []
        self.dimensions = dimensions
        self.num_particles = num_particles
        self.max_iterations = max_iterations

        err_best_g=-1                   # best error for group
        pos_best_g=[]                   # best position for group
        err_best_g_list=[]

        start_time = time.time()

        # establish the swarm
        swarm=[]
        for i in range(0,num_particles):
            swarm.append(Particle(self.dimensions))

        # begin optimization loop
        i=0
        while i < self.max_iterations:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,self.num_particles):
                swarm[j].evaluate(func_fitness)

                # determine if current particle is the best (globally)
                if swarm[j].err < err_best_g or err_best_g == -1:
                    pos_best_g=list(swarm[j].position)
                    err_best_g=float(swarm[j].err)

            #Saving the best error values
            err_best_g_list.append(err_best_g)
            self.error_history.append(err_best_g)

            # cycle through swarm and update velocities and position
            for j in range(0,self.num_particles):
                #swarm[j].update_velocity_intertia(pos_best_g)
                swarm[j].update_velocity_clerc(pos_best_g)
                swarm[j].update_position()
            i+=1

        self.convergence_time = time.time() - start_time
        self.best_error = err_best_g
        # update final results squared_error
        self.best_position = pos_best_g
