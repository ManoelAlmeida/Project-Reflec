from __future__ import division
import random
import math
import time
from Particle import Particle
from utils import Configuration

class PSO():
    def __init__(self,func_fitness):
        err_best_g=-1                   # best error for group
        pos_best_g=[]                   # best position for group
        err_best_g_list=[]
        self.best_position = []

        start_time = time.time()
        result=[]
        # establish the swarm
        swarm=[]
        for i in range(0,Configuration().num_particles):
            swarm.append(Particle())

        # begin optimization loop
        i=0
        while i < Configuration().max_iterations:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,Configuration().num_particles):
                swarm[j].evaluate(func_fitness)

                # determine if current particle is the best (globally)
                if swarm[j].err < err_best_g or err_best_g == -1:
                    pos_best_g=list(swarm[j].position)
                    err_best_g=float(swarm[j].err)

            #Saving the best error values
            err_best_g_list.append(err_best_g)
            result.append(','.join(str(e) for e in  swarm[j].position) + ',' + str(err_best_g))
            print(err_best_g)

            # cycle through swarm and update velocities and position
            for j in range(0,Configuration().num_particles):
                swarm[j].update_velocity_intertia(pos_best_g)
                #swarm[j].update_velocity_clerc(pos_best_g)
                #swarm[j].update_position(bounds)
                swarm[j].update_position()
            i+=1

        result.append(time.time() - start_time)
        #self.save_convergence(err_best_g_list)
        self.save_convergence(result)

        # print final resultssquared_error
        print('Best position: ', pos_best_g)
        print('Best error: ', err_best_g)
        self.best_position = pos_best_g

    def save_convergence(self, error_list):
        with open("./results/error_list_particles_"
                  +str(Configuration().num_particles)+
                  "_iterations_"+str(Configuration().max_iterations)+".txt", "w") as file:
            for r in error_list:
                file.write(str(r))
                file.write('\n')
