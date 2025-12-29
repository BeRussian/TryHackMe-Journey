## HELP POWERSHELL

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

## Move in the system
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

## Use properties
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

## System info
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

# Get all system proccess currently running
Get-Process
# GEt all services currently running on system
Get-Service
# Get net connection (similar to netstat -ano )


get-FileHash -Path .\$FILE

# Check alternate data stream (ADS)
Get-Item -Path "$FILE" -Stream *

# Run local script on other computer using remote connection 
 Invoke-Command -FilePath $SCRIPT -ComputerName $IP

#Run a command on other computer 
Invoke-Command -ComputerName $IP -Credential $USERNAME\$PASS -ScriptBlock { $COMMAND }
