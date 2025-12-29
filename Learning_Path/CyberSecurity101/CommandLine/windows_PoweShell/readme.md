## Walkthrough of Windows PowerShell



## Theory - What will we learn?
* Learn what PowerShell is and its capabilities
* Understand the basic structure of PowerShell’s language.
* Learn and run some basic PowerShell commands
* Understand PowerShell’s many applications in the cyber security industry.



### What is powershell
* scripting language
* Used for automation of simple task and cinfiguration managment
* Built on .NET framework -->Tool set of windows
* PowerShell is Object-oriented
* Each "object" has:
    * Properties 
    * Methods -> Functions the object can to 
    * example: 
```
Car object:
properties: color, model, FuelLevel
Methods: Drive, Honk, Refuel
```
* Started as exlusive to Windows, but today supports also macOS and Linux

#### Q: What do we call the advanced approach used to develop PowerShell?
#### A: object-oriented
## Basic Powershell
* 2 ways to lunch
1. Write powershell inside `cmd`
2. Open powershell application in windowsc search

```ps1
#Print all avalible commands
Get-Command
#Print all avalible command with type=function
Get-Command -CommandType "Function"

#Get more info on specific command
Get-Help $COMMAND
Get-Help Get-Date
#Get examples on how to use command
Get-Help New-LocalUser -examples


#Get all alias of commands
Get-Alias
#Get alias of spesific command
Get-Alias echo

#Find addtional libraries&Modules
Find-Module -Name "PowerShell*"
#Download the wanted module
Install-Module -Name "PowerShellGet"

```
#### Q:How would you retrieve a list of commands that start with the verb Remove? [for the sake of this question, avoid the use of quotes (" or ') in your answer]
#### A: `Get-Command -Name Remove*`

#### Q:What cmdlet has its traditional counterpart echo as an alias?
#### A: `Write-Output`

#### Q:What is the command to retrieve some example usage for the cmdlet New-LocalUser?
#### A: `Get-Help New-LocalUser -examples`

##
```ps1
#ls/dir
Get-ChildItem

#cd
Set-Location -Path ".\Documents"

#mkdir
New-Item -Path ".\captain-cabin\captain-wardrobe" -ItemType "Directory"

#create empty file
New-Item -Path ".\captain-cabin\captain-wardrobe\captain-boots.txt" -ItemType "File"

#Delete file(Workes on both files and directories)
Remove-Item -Path ".\captain-cabin\captain-wardrobe\"

#cp
Copy-Item -Path .\captain-hat.txt -Destination .\captain-hat2.txt

#mv
Move-Item -Path $FROM -Destination $TO 

#cat
Get-Content -Path ".\captain-hat.txt"
```

#### Q:What cmdlet can you use instead of the traditional Windows command type?
#### A:`Get-Content`

#### Q:What PowerShell command would you use to display the content of the "C:\Users" directory?
#### A:` Get-ChildItem -Path C:\Users`

#### Q:How many items are displayed by the command described in the previous question?
```ps1

              Administrator
              captain
              p1r4t3
               Public

```
#### A:`4`
## Piping
```ps1
# ls and sort by file size
Get-ChildItem | Sort-Object Length
# ls and print only text files
Get-ChildItem | Where-Object -Property "Extension" -eq ".txt" 
# ls and find file that contain $WORD
Get-ChildItem | Where-Object -Property "Name" -like "$WORD*"

## ls and only print name and file size
Get-ChildItem | Select-Object Name,Length

#ls| sort by file size | and print largets file
Get-ChildItem | Sort-Object length -Descending | Select-Object -First 1

#grep
Select-String -Path ".\captain-hat.txt" -Pattern "hat"
```

#### Q: How would you retrieve the items in the current directory with size greater than 100?
#### A: `Get-ChildItem | Where-Object -Property Length -gt 100 `

##
## System commands
```ps1
# Get info about host
Get-ComputerInfo
# Shorter info
systeminfo
# List all local users
Get-LocalUser
#get network info -> ipconfig
Get-NetIPConfiguration
# Display all ip address of system
Get-NetIPAddress
```
#### Q: Other than your current user and the default "Administrator" account, what other user is enabled on the target machine?
* Lets print all users with `Get-LocalUser`
```
p1r4t3             True    A merry life and a short one.

```
#### A: `p1r4t3`

#### Q: This lad has hidden his account among the others with no regard for our beloved captain! What is the motto he has so bluntly put as his account's description?
#### A: `A merry life and a short one.`

#### Q: Now a small challenge to put it all together. This shady lad that we just found hidden among the local users has his own home folder in the "C:\Users" directory. Can you navigate the filesystem and find the hidden treasure inside this pirate's home?
* lets cd to `cd C:\Users\p1r4t3\`
* lets print contents of `p1r4t3` home directory --> `Get-ChildItem`
* we see intresting directory named `hidden-treasure-chest`, lets check what inside --> `Get-ChildItem`
* what is this file `big-treasure.txt`? lets check
#### A: `THM{p34rlInAsh3ll}`


##
```ps1
# Get all system proccess currently running
Get-Process
# GEt all services currently running on system
Get-Service
# Get net connection (similar to netstat -ano )


get-FileHash -Path .\$FILE

# Check alternate data stream (ADS)
Get-Item -Path "$FILE" -Stream *

```

#### Q: In the previous task, you found a marvellous treasure carefully hidden in the target machine. What is the hash of the file that contains it?
`Get-FileHash .\big-treasure.txt`
#### A: `71FC5EC11C2497A32F8F08E61399687D90ABE6E204D2964DF589543A613F3E08`

#### Q:What property retrieved by default by Get-NetTCPConnection contains information about the process that has started the connection?
* Lets use this command and check properties

`Get-NetTCPConnection`
```ps1
LocalAddress                        
LocalPort 
RemoteAddress                       
RemotePort State       
AppliedSetting 
OwningProcess
```
#### A: `OwningProcess`
#### Q: It's time for another small challenge. Some vital service has been installed on this pirate ship to guarantee that the captain can always navigate safely. But something isn't working as expected, and the captain wonders why. Investigating, they find out the truth, at last: the service has been tampered with! The shady lad from before has modified the service DisplayName to reflect his very own motto, the same that he put in his user description.

With this information and the PowerShell knowledge you have built so far, can you find the service name?  
* Lets print all system services with

`Get-Service`
* damm we see many services, lets try to filter that

```ps1
Get-Service | Where-Object -Property "DisplayName" -like "*merry life*"

#Output:
Running  p1r4t3-s-compass   A merry life and a short one.
```
#### A: `p1r4t3-s-compass`

##
## Invoke

```ps1
# Run local script on other computer using remote connection 
 Invoke-Command -FilePath $SCRIPT -ComputerName $IP

#Run a command on other computer 
Invoke-Command -ComputerName $IP -Credential $USERNAME\$PASS -ScriptBlock { $COMMAND }
```

#### Q:What is the syntax to execute the command Get-Service on a remote computer named "RoyalFortune"? Assume you don't need to provide credentials to establish the connection. [for the sake of this question, avoid the use of quotes (" or ') in your answer] 

#### A: `Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }`


##
#### Q: 

#### A: ``


##


## You completed the room!!!