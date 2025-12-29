## Walkthrough for Advent of Cyber 2025 - Day 1


Very easy challenge, just need to find file hidden on the system
We get a hint on `README.txt` file in the ~ directory
we are looking for a guide that is hidden
lets go to the `Guides` directory and look for hidden files

`ls -a Guides`
we see a `.guide.txt` file
lets read it using cat

Flag --> THM{learning-linux-cli}

Next flag we need to find scipt named `eggstrike`
`find /home/ -name 'egg'`
After some searching i found it inside `/home/socmas/2025`
lets cat it
`cat eggstrike.sh`
Flag --> THM{sir-carrotbane-attacks}


We got another root flag
For that lets switch to the root user
`sudo su`
we get hint in the question that the flag is in the history
lets check the history of the root user
`history`
Flag --> THM{until-we-meet-again}







