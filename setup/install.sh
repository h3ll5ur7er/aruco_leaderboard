sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install -y build-essential cmake unzip pkg-config
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran

sudo apt-get install -y python3-dev
sudo apt-get install -y python3-pip

sudo pip3 install flask-restplus sqlalchemy numpy

git clone https://github.com/opencv/opencv
git clone https://github.com/opencv/opencv_contrib
git clone https://github.com/h3ll5ur7er/aruco_leaderboard

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