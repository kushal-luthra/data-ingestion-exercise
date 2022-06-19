#!/usr/bin/env bash


__install() {
    sudo apt update;
    sudo apt --yes install software-properties-common;
    sudo add-apt-repository ppa:deadsnakes/ppa;
    sudo apt update; sudo apt --yes install python3.7;
    sudo rm /usr/bin/python3;
    sudo ln -s /usr/bin/python3.7 /usr/bin/python3
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py;
    python3 get-pip.py --force-reinstall;
    sudo apt-get --yes install python3.7-dev;
    sudo apt-get --yes install libpq-dev;
    pip3 install virtualenv;
    virtualenv -p python3 venv;
}

__zip() {
    curr_dir=${PWD##*/}

    echo "Build package"
    mkdir -p dist && rm -rf dist/*
    cd .. && zip -r ${curr_dir}/dist/${curr_dir}.zip ${curr_dir} -x '*.git*' '*cache*' '*dist*' '*.DS_Store*' '*Makefile*'
    echo "Done"
}

"$@"