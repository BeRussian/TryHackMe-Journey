## Walkthrough of DAY 14 - Container Security



## Theory - What will we learn?
* Learn about Containers and Docker work ( including images, layers, and the container engine)
* Explore Docker runtime concepts (sockets, daemon API) and common container escape/privilege-escalation vectors
* Apply these skills to investigate image layers, escape a container, escalate privileges, and restore the DoorDasher service

### What is a container
* Insead of just Using the apllication, containers contain moreover all the dependencies to run an application
* Similar to Virtual Machines, only more Lightweight(Dont have a seperate OS, uses the host OS)
* Faster to start
* containers excel at deploying scalable, portable micro-services.

### architecture
`Virtual Machines`
Infrastructture -> Hypervisor ---> Guest OS -> bins/Lib -> Applications

`Containers`
Infrastructture -> Host Operatins system > Container engine -> Applications(bins/Lib are inside)

`Microservices`
* The ability to divide application into parts, each has its uniq container

`Conainer engine` 
*  Software that builds, runs, and manages containers by leveraging the host system's OS kernel
* Example of Container engine --->>`docker`

`Docker`
* Open source platform, allows developers to build , deploy and manage containers
* Uses 
    * Dockerfile --> The recipe
    ### Answer to question 2 `dockerfile`
    * image --> The ingreidiants
    * container -> The meal

`Docker Daemon`
* application the runs on host and manages all the containers
* Has root privileges to all the containers

`Socket`
* Thats how users talk to the Daemon
* its a file `/var/run/docker.sock` allows the host pc talk with the daemon
* If badly confidured and socket file is given access to a spesific container, Its Causes a vulnerability named `Escape Attack`

### Practical
lets dive into the docker and try to perform an escape attack

`docekr ps` allows us to check all running containers
### Answer to question 1 `docekr ps`
`docker exec -it uptime-checker sh`
Allows us to go inside the uptime-checker container
* exec --> Run a command
* -it ---> interactive mode
* sh --> generate a simple shell


`ls -la /var/run/docker.sock`
* check if socket is found inside this container
* If does, It allows us to control the deamon
* We can check it works by running docker commands from inside the container
`docker ps` --> Workes!!!

Lets exploit the vulnerability
`docker exec -it deployer bash` --> from inside the uptime-checker container --> Success

Lets check who we are --> deployer

Now lets just Find the script located in /flag.txt


### Answer to question 3 `THM{DOCKER_ESCAPE_SUCCESS`

##
## Answers
#### Q:  What exact command lists running Docker containers?



#### A: `docker ps`

##
#### Q: What file is used to define the instructions for building a Docker image?



#### A: `Dockerfile`


##
#### Q: What's the flag?



#### A: `THM{DOCKER_ESCAPE_SUCCESS}`

##
#### Q: There is a secret code contained within the news site running on port 5002; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it?
* go to `http://10.66.180.209:5002/`
* There are 3 highlited word, combine them

#### A: `DeployMaster2025!`


## You completed the room!!!