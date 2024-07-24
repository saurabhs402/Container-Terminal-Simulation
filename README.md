# Container Terminal Simulation

This repository contains a simulation of a container terminal using SimPy. The simulation models the process of vessels arriving at the terminal, berthing, unloading containers using quay cranes, and transporting containers using terminal trucks.

## Simulation Details

### Features

- **Vessel Arrival**: Vessels arrive at the terminal following an exponential distribution with an average of 5 hours between arrivals.
- **Berths**: The terminal has 2 berths. Vessels wait if both berths are occupied.
- **Quay Cranes**: There are 2 quay cranes, each capable of unloading containers from any berth. Each vessel uses one crane at a time, and each container takes 3 minutes to unload.
- **Trucks**: The terminal has 3 trucks for transporting containers from quay cranes to yard blocks. Each trip takes 6 minutes.
- **Event Logging**: The simulation logs key events, including vessel arrivals, berthing, container unloading, and container transportation, with timestamps.
### Clone the Repository

```
git clone https://github.com/saurabhs402/Container-Terminal-Simulation.git
```

### Installation

To run the simulation, you need Python installed on your system. The only dependency required is SimPy, which can be installed via pip.

```
python -m venv venv
venv\Scripts\activate
```
```
pip install -r requirements.txt
```
```
python main.py
```
## Code Overview

- vessel_generator: Generates vessels arriving at the terminal based on an exponential distribution.
- activity_berth: Represents a vessel arriving at the terminal, berthing, and unloading containers.
- activity_crane_truck: Handles the process of unloading containers using quay cranes and transporting them using trucks.

- run_simulation: Sets up the simulation environment, initializes resources, and runs the simulation.



## Simulation Logic
1. Vessel Generator:

   - Generates vessels at intervals based on an exponential distribution.
   - Initiates the activity_berth process for each arriving vessel.

2. activity_berth Process:

   - Requests a berth and starts unloading containers once berthed.
   - Initiates the activity_crane_truck process to unloads containers using a quay crane, 
     then loads containers onto a truck for transportation.
   - Releases the berth once unloading is complete.

3. activity_crane_truck Process:

   - Requests a quay crane and unloads a container.
   - Requests a truck and transports the container to the yard block.
   - Releases the crane and truck resources after use.

4. Run Simulation:

   - Sets up the simulation environment and resources.
   - Starts the vessel generator process.
   - Runs the simulation for the specified duration.

## Example Output
```
Vessel 1 arrives at the terminal : 0
Vessel 1 is berthing: 0
Vessel 1 starts unloading a container: 0
Vessel 1 loads a container onto a truck: 3
Vessel 1 starts unloading a container: 9
Vessel 1 loads a container onto a truck: 12
Vessel 1 starts unloading a container: 18
Vessel 1 loads a container onto a truck: 21
Vessel 1 starts unloading a container: 27
Vessel 1 loads a container onto a truck: 30
Vessel 1 starts unloading a container: 36
Vessel 1 loads a container onto a truck: 39
Vessel 1 starts unloading a container: 45
Vessel 1 loads a container onto a truck: 48
Vessel 1 starts unloading a container: 54
Vessel 1 loads a container onto a truck: 57
Vessel 1 starts unloading a container: 63
Vessel 1 loads a container onto a truck: 66
Vessel 1 starts unloading a container: 72
Vessel 1 loads a container onto a truck: 75
Vessel 1 starts unloading a container: 81
Vessel 1 loads a container onto a truck: 84
Vessel 1 starts unloading a container: 90
Vessel 1 loads a container onto a truck: 93
Vessel 1 starts unloading a container: 99
Vessel 1 loads a container onto a truck: 102
Vessel 1 starts unloading a container: 108
Vessel 1 loads a container onto a truck: 111
Vessel 1 starts unloading a container: 117
Vessel 1 loads a container onto a truck: 120
Vessel 1 starts unloading a container: 126
Vessel 1 loads a container onto a truck: 129
Vessel 2 arrives at the terminal : 133.68282689808854
Vessel 2 is berthing: 133.68282689808854
Vessel 2 starts unloading a container: 133.68282689808854
Vessel 1 starts unloading a container: 135
Vessel 2 loads a container onto a truck: 136.68282689808854
Vessel 1 loads a container onto a truck: 138
Vessel 2 starts unloading a container: 142.68282689808854
Vessel 1 starts unloading a container: 144
Vessel 2 loads a container onto a truck: 145.68282689808854
Vessel 1 loads a container onto a truck: 147
Vessel 2 starts unloading a container: 151.68282689808854
Vessel 1 starts unloading a container: 153
Vessel 2 loads a container onto a truck: 154.68282689808854
Vessel 1 loads a container onto a truck: 156
Vessel 2 starts unloading a container: 160.68282689808854
Vessel 1 starts unloading a container: 162
Vessel 2 loads a container onto a truck: 163.68282689808854
Vessel 1 loads a container onto a truck: 165
Vessel 2 starts unloading a container: 169.68282689808854
Vessel 1 starts unloading a container: 171
Vessel 2 loads a container onto a truck: 172.68282689808854
Vessel 1 loads a container onto a truck: 174
Vessel 2 starts unloading a container: 178.68282689808854
Vessel 1 starts unloading a container: 180
Vessel 2 loads a container onto a truck: 181.68282689808854
Vessel 1 loads a container onto a truck: 183
Vessel 2 starts unloading a container: 187.68282689808854
Vessel 1 starts unloading a container: 189
Vessel 2 loads a container onto a truck: 190.68282689808854
Vessel 1 loads a container onto a truck: 192
Vessel 2 starts unloading a container: 196.68282689808854
Vessel 1 starts unloading a container: 198
Vessel 2 loads a container onto a truck: 199.68282689808854
Vessel 1 loads a container onto a truck: 201
Vessel 2 starts unloading a container: 205.68282689808854
Vessel 1 starts unloading a container: 207
Vessel 2 loads a container onto a truck: 208.68282689808854
Vessel 1 loads a container onto a truck: 210
Vessel 2 starts unloading a container: 214.68282689808854
Vessel 1 starts unloading a container: 216
Vessel 2 loads a container onto a truck: 217.68282689808854
Vessel 1 loads a container onto a truck: 219
Vessel 2 starts unloading a container: 223.68282689808854
Vessel 1 starts unloading a container: 225
Vessel 2 loads a container onto a truck: 226.68282689808854
Vessel 1 loads a container onto a truck: 228
Vessel 2 starts unloading a container: 232.68282689808854
Vessel 1 starts unloading a container: 234
Vessel 2 loads a container onto a truck: 235.68282689808854
Vessel 1 loads a container onto a truck: 237
Vessel 2 starts unloading a container: 241.68282689808854
Vessel 1 starts unloading a container: 243
Vessel 2 loads a container onto a truck: 244.68282689808854
Vessel 1 loads a container onto a truck: 246
Vessel 2 starts unloading a container: 250.68282689808854
Vessel 1 starts unloading a container: 252
Vessel 2 loads a container onto a truck: 253.68282689808854
Vessel 1 loads a container onto a truck: 255
Vessel 2 starts unloading a container: 259.68282689808854
Vessel 1 starts unloading a container: 261
Vessel 2 loads a container onto a truck: 262.68282689808854
Vessel 1 loads a container onto a truck: 264
Vessel 2 starts unloading a container: 268.68282689808854
Vessel 1 starts unloading a container: 270
Vessel 2 loads a container onto a truck: 271.68282689808854
Vessel 1 loads a container onto a truck: 273
Vessel 3 arrives at the terminal : 273.36151404057864
Vessel 2 starts unloading a container: 277.68282689808854
.....
.....
Simulation ends:1198.6828268980885

```
