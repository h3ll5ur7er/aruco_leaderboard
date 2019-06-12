# Aruco  RC-Leaderboard

## Database schema


```puml
@startuml

class Event{
    date
}
class Race{
    name
}
class Lap{
    number
}

class Team{
    name
}
class Driver{
    name
}
class Category<TODO>{
    name
}
class Car{
    marker_id
}

class Result{
    start
    end
}

Event "1" --> "*" Race : has multiple
Race "1" --> "*" Lap : can have multiple
Team "1" --> "*" Driver : aggregates
Driver "1" --> "*" Car : can have multiple
Category "1" --> "*" Car : categorizes
Car "1" -left-> "*" Result : achieves
Lap "1" -right-> "*" Result: belongs to

@enduml
```

## Installation instructions
- download the latest version of [rasbian](https://downloads.raspberrypi.org/raspbian_lite_latest) and flash it to the micro sd card (using a tool like [etcher](https://www.balena.io/etcher/)).
- inside the boot partition of the sdcard (the one available on windows) do the following:
    - create a empty text file called ```ssh```
    - if you want the pi to automatically connect to wifi edit the content of the file ```wpa_supplicant.conf```:
        - set the appropriate country code (most likely ```CH```)
        - edit the ssid (network name) to fit your wifi.
        - edit the psk (pre-shared key, password) to fit your wifi.
        - when done copy the file to the boot partition of your sdcard.
    - copy ```install.sh```, ```dphys-swapfile``` and ```aruco_leaderboard.service``` to the boot partition of your sdcard.
    - connect to the pi using ssh (PuTTY or the ssh commandline tool)
        - default username: pi
        - default password: raspberry
    - run ```sudo apt-get update```
    - run ```sudo apt-get dist-update```
    - run ```sudo rpi-update```
        - confirm with ```y``` when prompted
    - reboot the pi using ```sudo reboot```
    - after some seconds reconnect via ssh
    - run ```sudo mv /etc/dphys-swapfile /etc/dphys-swapfile.orig```
    - run ```sudo cp /boot/dphys-swapfile /etc/dphys-swapfile```
    - run ```sudo /etc/init.d/dphys-swapfile stop```
    - run ```sudo /etc/init.d/dphys-swapfile start```
    - run ```sudo /boot/install.sh``` (takes a while)
    - to check if everything worked run ```python3 -c "import cv2;print(cv2.__version__)"``` this should show the curernt opencv version number (example: 4.1.0-dev)
    - run ```sudo cp /boot/aruco_leaderboard.service /lib/systemd/system/aruco_leaderboard.service```
    - run ```sudo systemctl enable aruco_leaderboard.service```
    - run ```sudo systemctl start aruco_leaderboard.service```
    - using a webbrowser connect to the ip-address of the pi. this should show you the api-definition via swagger-ui


## Label generator
- **Font:** FONT_HERSHEY_DUPLEX
- **Output mockup**
    - **#**: ar marker
    - **%**: background image
    - **&**: starting number

```plain
    +------------------------------------+
    | # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% # |
    +------------------------------------+
    |   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   |
    |   %%%&&&&&&&&&&&&&&&&&&&&&&&&%%%   |
    |   %%%&&&&&&&&&&&&&&&&&&&&&&&&%%%   |
    |   %%%&&&&&&&&&&&&&&&&&&&&&&&&%%%   |
    |   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   |
    +------------------------------------+
    | # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% # |
    +------------------------------------+
```

- **Parameters**
    - **aruco_code_1** = integer[0-999]
    - **aruco_code_2** = integer[0-999]
    - **aruco_code_3** = integer[0-999]
    - **aruco_code_4** = integer[0-999]
    - **starting_number** = integer[0-999]
    - **background_image** = image_path
    - **top_bar_color** = color (r,g,b)
    - **bottom_bar_color** = color (r,g,b)
### Installation:
#### Installation:
- install python from [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86_64.exe)
- ~~download opencv package~~
- ~~install opencv package~~
### usage:
- ~~download label_generator.py~~
- run ```python label_generator.py id1 id2 id3 id4 starting_number image_path top_color bottom_color```
  - example ```python label_generator.py 1 23 45 678 678 ./testimage.png (255,0,0) (255,0,0)```