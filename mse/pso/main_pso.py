from PSO import PSO

# Sphere Function
def Sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total

def Rosenbrock(x):
    total=0
    for i in range(len(x)):
        total += ((100 * (x[i] - x[i]**2)**2) + (x[i] - 1)**2)
    return total


if __name__ == "__PSO__":
    main()


initial=[5,5]               # initial starting location [x1,x2...]
bounds=[(-10,10),(-10,10)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
#PSO(Sphere,initial,bounds,num_particles=15,maxiter=30)
PSO(Rosenbrock,initial,bounds,num_particles=15,maxiter=3000)