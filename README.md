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
class Car{
    marker_id
}

class Result{
    start
    end
}

Event "1" --> "*" Race
Race "1" --> "*" Lap
Team "1" -- > "*" Driver
Driver "1" --> "*" Car
Car "1" -left-> "*" Result
Lap "1" -right-> "*" Result

@enduml
```

## OpenCV build instructions

```bash
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install -y build-essential cmake unzip pkg-config
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran

sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xf Python-3.7.0.tar.xz
cd Python-3.7.0
./configure --prefix=/usr/local/opt/python-3.7.0
make -j 4

sudo make altinstall

sudo ln -s /usr/local/opt/python-3.7.0/bin/pydoc3.7 /usr/bin/pydoc3.7
sudo ln -s /usr/local/opt/python-3.7.0/bin/python3.7 /usr/bin/python3.7
sudo ln -s /usr/local/opt/python-3.7.0/bin/python3.7m /usr/bin/python3.7m
sudo ln -s /usr/local/opt/python-3.7.0/bin/pyvenv-3.7 /usr/bin/pyvenv-3.7
sudo ln -s /usr/local/opt/python-3.7.0/bin/pip3.7 /usr/bin/pip3.7
alias python='/usr/bin/python3.7'
alias python3='/usr/bin/python3.7'
ls /usr/bin/python*
cd ..
sudo rm -r Python-3.7.0
rm Python-3.7.0.tar.xz
. ~/.bashrc


pip3 install numpy

git clone https://github.com/opencv/opencv
git clone https://github.com/opencv/opencv_contrib

mkdir opencv_build
cd opencv_build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DINSTALL_PYTHON_EXAMPLES=ON \
    -DINSTALL_C_EXAMPLES=OFF \
    -DBUILD_DOCS=OFF -D BUILD_PERF_TESTS=OFF \
    -DBUILD_TESTS=OFF \
    -DOPENCV_ENABLE_NONFREE=ON \
    -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
    -DPYTHON_EXECUTABLE=/usr/local/opt/python-3.7.0/bin/python3.7 \
    -DPYTHON3_EXECUTABLE=/usr/local/opt/python-3.7.0/bin/python3.7 \
    -DPYTHON_DEFAULT_EXECUTABLE=/usr/local/opt/python-3.7.0/bin/python3.7 \
    -DPYTHON_INCLUDE_DIR=/usr/local/opt/python-3.7.0/include/python3.7 \
    -DPYTHON_INCLUDE_DIR2=/usr/local/opt/python-3.7.0/include/python3.7m \
    -DPYTHON_LIBRARY=/usr/local/opt/python-3.7.0/lib/libpython3.7m.a \
    -DPYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/opt/python-3.7.0/lib/python3.7/site-packages/numpy/core/include \
    -DBUILD_opencv_python2=OFF \
    -DBUILD_opencv_python3=ON \
    -DBUILD_EXAMPLES=ON ../opencv
# make -j4
make -j8
sudo make install
sudo ldconfig
cd ..
rm -r opencv
rm -r opencv_contrib
```

## FONT_HERSHEY_DUPLEX

cmake -D CMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DINSTALL_PYTHON_EXAMPLES=ON -DINSTALL_C_EXAMPLES=OFF -DBUILD_DOCS=OFF -D BUILD_PERF_TESTS=OFF -DBUILD_TESTS=OFF -DOPENCV_ENABLE_NONFREE=ON -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -DBUILD_opencv_python2=OFF -DBUILD_opencv_python3=ON -DBUILD_EXAMPLES=ON ../opencv