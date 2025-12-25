## Walkthrough of Day 19 - ICS/Modbus - Claus for Concern 



## Theory - What will we learn?
* How SCADA (Supervisory Control and Data Acquisition) systems monitor industrial processes
* What PLCs (Programmable Logic Controllers) do in automation
* How the Modbus protocol enables communication between industrial devices
* How to identify compromised system configurations in industrial systems
* Techniques for safely remediating compromised control systems
* Understanding protection mechanisms and trap logic in ICS environments

`ICS` --> "Industrial Control Systems" , The entire machines in the organization
`PLC` --> "Programmable Logic Controller" , small computer that manages the operations
`SCADA`-> "Supervisory Control and Data Acquisition", program that controls all the PLS
`Modbus` -> Procotol, The language in which the SCADA and the PLC's talking to each other
* Modbus is very old and unsecure protocol 
### SCADA
SCADA systems usually have 4 key components:
1. Sensors & Actuators
    * Sensors Measure (Temp,Pressure, Weight , etc...)
    * Actuators move things according to the measures done by the sensors
    * Pizza Example: Oven that measure the Temp at all time, If it pass 300, Turns of the gas
    * Sensore reads the Temp, Actuators controls the gas
2. PLC
    * Take in the input from the Sensors
    * Act as the brain and make decisions based on written rules
    * Send instructaions to the Actuators
    * In our example:
    * PLC can decide: If a package weight = Chocolate egg and Destination is 5, Put it on drone7
3. Monitoring systems
    * All the things required to make sure everything is running smoothly
    * In a factory it will be(CCTV cameras, dashboards and alarms)
    * Most time real humans will operate and control this systems
4. Historians
    * As soc teams saves all the logs for later inspectaions
    * SCADA systems shuld preserve all data about every automation
    * Later could be inspected if something went wrong

### Why attacker love SCADA
* Most times they operate on old systems
* Use defult credentials
* Built before world new what is cyber attacks
* Has real world Consequences
* Many times connected to the Organizations network
* Protocols like modbus doesnt use authentication

### Real world case
* In early 2024 ICS/OT malware first discoverd by cyber company Dragos
* Written in Golang(allows to run on both linux and windows)
* This malware could directly control ICS systems and inject malicous commands
#### Attack on Lviv (Ukraine)
In january 2024, Malicous attackers used `FrostyGoop` to attack The entire city's heating system
* It caused over 600 Building to stop heating for over 48 hours in below zero tempratures


##
#### Q: What port is commonly used by Modbus TCP?

#### A: `502`


### PLC Vs PC
* PLC's are industrial computers
* Built for spesific porpuse 
* Created for extreme reliability and harsh conditions
    * Build to servive Harsh temperatures, Earthquakes,  Water and more
    * Run nonstop 24/7 without interference for decades
    * Reacts to input from sensorst in milliseconds
    * Talk straight with Sensors and Actuators

### Modbus
* One of the first protocols used in industrial enviroments.
* Old but simple , reliable and workes on many systems
* Works in GET/POST methods
* Example:

Client (your computer): "PLC, what's the current value of register 0?"
Server (the PLC): "Register 0 currently holds the value 1."
* Valuable note --> There is no authantication!

Sorts data in 4 data types:
* Coils (Output)
    * 0 or 1
    * Example: Motor running?Alarm Active?
* Discrete Inputs
    * 0 or 1
    * Example: Motor running?Alarm Active?
* Holding Registers (Output)
    * 0 - 65535
* Input Registers
    * 0-65535

*NOTE* 

*Coils and Holding Registers are writable*

*Discrete Inputs and Input Registers are read-only*

## Practical
* Once the machine is UP i did basic nmap scan

`nmap 10.65.154.75 -T4 -p- -Pn`
```bash
#Output
22/tcp    open  ssh
80/tcp    open  http
102/tcp   open  iso-tsap
502/tcp   open  mbap
8080/tcp  open  http-proxy
44818/tcp open  EtherNetIP-2

```
Lets investigate the open ports even more

`nmap -Pn 10.65.154.75 -T4 -sC -sV -p 22,80,102,502,8080,44818
`
* Output is saved in `extendedNmap`

* port 80 connect to CCTV
* port 8080 is login page
* port 502 indicate a modbus protocol is active

lets check the note from the beggining of the room
```
TBFC DRONE CONTROL - REGISTER MAP
(For maintenance use only)

HOLDING REGISTERS:
HR0: Package Type Selection
     0 = Christmas Gifts
     1 = Chocolate Eggs
     2 = Easter Baskets

HR1: Delivery Zone (1-9 normal, 10 = ocean dump!)

HR4: System Signature/Version
     Default: 100
     Current: ??? (check this!)

COILS (Boolean Flags):
C10: Inventory Verification
     True = System checks actual stock
     False = Blind operation

C11: Protection/Override
     True = Changes locked/monitored
     False = Normal operation

C12: Emergency Dump Protocol
     True = DUMP ALL INVENTORY
     False = Normal

C13: Audit Logging
     True = All changes logged
     False = No logging

C14: Christmas Restored Flag
     (Auto-set when system correct)

C15: Self-Destruct Status
     (Auto-armed on breach)

CRITICAL: Never change HR0 while C11=True!
Will trigger countdown!

- Maintenance Tech, Dec 19
```


### Modbus Reconnaissance 
1. Install PyModbus

`pip3 install pymodbus==3.6.8 --break-system-packages`

#### I have added few script into this directory
1. `connect.py` --> simply check connection to the `modbus` service
2. `read_Holding_Register.py` simple script i personaly written to read modbus data base
3. `FullReconissance` Scipt given by room to scan full database for info
4. `fix_Everything.py` Script you need to run to get the flag
`python fix_Everything.py`

### Flag --->
### `Flag: THM{eGgMas0V3r}`


##


## You completed the room!!!