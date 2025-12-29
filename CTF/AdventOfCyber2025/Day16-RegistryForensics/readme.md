## Walkthrough of Day 16 - Forensics - Registry Furensics 



## Theory - What will we learn?
* Understand what the Windows Registry is and what it contains.
* Dive deep into Registry Hives and Root Keys.
* Analyze Registry Hives through the built-in Registry Editor tool.
* Learn Registry Forensics and investigate through the Registry Explorer tool.


### Tools
Registry Editor (regedit) --> Built-In windows system
Rehistry Explorer --> Help us do a forensics work on files of RAM

### HIVES
* System (Services, Mounted devices, Boot Configirations, Drivers, Hardware)
    * C:\Windows\System32\config\SYSTEM
* Security (Local Security Policies , Audit Policy settings) 
    * C:\Windows\System32\config\SECURITY
* Software (Installed programs, OS version and info, Autstarts programs, Programs settings)
    * C:\Windows\System32\config\SOFTWARE
* SAM (Usernames and their Metadata , Password hash's Group memberships & accound statuses) 
    * C:\Windows\System32\config\SAM
* NTUSER.DAT (Recent Files , User Preferences, User-specific Autostarts)
    * C:\Users\username\NTUSER.DAT
* USRCLASS.DAT (Shellbags , Jump Lists) 
    * C:\Users\username\AppData\Local\Microsoft\Windows\USRCLASS.DAT

#### Note
* This hives store keys in binary, you cant just open them
* You need to use application like `Registry Editor (RegEdit)` 
* HKEY_LOCAL_MACHINE(SYSTEM,SECURITY,SOFTWARE,SAM)
* HKEY_USERS/HKEY_CURRENT_USER(HKEY_CURRENT_USER , USRCLASS.DAT)


### Practical

#### USB
* Devices connected to PC via USB
    * HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR
#### Files&Applications
* View Programs Run by the User (Only using `Win + R`)
    * HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
* Programs (GUI) recently accessed by user
    * HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist
* Files recently accessed by user
    * HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
* All startup programs(starts at boot)
    * HKLM\Software\Microsoft\Windows\CurrentVersion\Run

#### Strings&searches
* Path typed by the user in explorer search bar(and pressed `Enter`)
    * HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
* Path typed by the user in explorer search box(for recent search function)
    * HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery

#### General Info
* Full path of All Applications
    * HKLM\Software\Microsoft\Windows\CurrentVersion\App Paths
* Computer name
    * HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
* Info on installed programs
    * HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

### Registry Explorer
* Allows to load offline hive for forensics investigation

##
## Answers
* Open `Registry Explorer`
* Load all hives from `C:\Users\Administrator\Desktop\Registry Hives`
#### Q: What application was installed on the dispatch-srv01 before the abnormal activity started?

 * Open `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
 * This key stores info about installed programs
 * look for the program installed on 21/10/2025

#### A: `DroneManager Updater`

##
#### Q: What is the full path where the user launched the application (found in question 1) from?

* Lets use `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`
* Shows info about programs User ran Via GUI
* Search for DroneManager
#### A: `C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe`


##
#### Q: Which value was added by the application to maintain persistence on startup?

* `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
* Stores all programs set to start on boot
* look for DroneManager

#### A: `"C:\Program Files\DroneManager\dronehelper.exe" --background`


##


## You completed the room!!!