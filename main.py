import simpy
import random


def vessel_generator(env, berth, crane, truck, arrival_rate):
    vessel_count = 1
    while True:
        env.process(activity_berth(env, f'Vessel {vessel_count}', berth, crane, truck))
        yield env.timeout(random.expovariate(arrival_rate))
        vessel_count += 1
        

def activity_berth(env, name, berth, crane, truck):
    print(f'{name} arrives at the terminal : {env.now}')
    berth_request = berth.request()
    yield berth_request
    print(f'{name} is berthing: {env.now}')
    yield env.process(activity_crane_truck(env, name, crane, truck))
    berth.release(berth_request)

def activity_crane_truck(env, name, crane, truck):
    containers = 150
    while containers > 0:
        crane_request = crane.request()
        yield crane_request
        print(f'{name} starts unloading a container: {env.now}')
        yield env.timeout(3)  # Crane unloads a container in 3 minutes

        truck_request = truck.request()
        yield truck_request
        print(f'{name} loads a container onto a truck: {env.now}')
        yield env.timeout(6)  # Truck transports the container in 6 minutes

        crane.release(crane_request)
        truck.release(truck_request)
        
        containers -= 1

    print(f'{name} has finished unloading and leaves the terminal: {env.now}')



def run_simulation(simulation_time, arrival_rate):
    env = simpy.Environment()
    berth = simpy.Resource(env, capacity=2)
    crane = simpy.Resource(env, capacity=2)
    truck = simpy.Resource(env, capacity=3)
    env.process(vessel_generator(env, berth, crane, truck, arrival_rate))
    env.run(until=simulation_time)

if __name__ == '__main__':
    SIMULATION_TIME = 1200 # Run the simulation for 1200 minutes
    ARRIVAL_RATE = 1 / 300  # Average of 5 hours =300 minutes, lamda= 1/mean(avg)

    run_simulation(SIMULATION_TIME, ARRIVAL_RATE)
