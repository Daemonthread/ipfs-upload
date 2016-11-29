# IPFS Upload
A small experiment with IPFS

### How to run on Ubuntu 16.04
Install dependencies from apt:

  ```
  sudo apt-get install libsqlite3-dev sqlite3 python-pip
  ```

Follow the instructions for how to get IPFS working on your system: https://ipfs.io/docs/install/

Clone the repo and install the required python packages with pip

  ```
  sudo pip install -r requirements.txt
  ```

Decide on your IPFS folder and export it:

  ```
  export IPFS_PATH=/home/toby/ipfs
  ```

Start your IPFS daemon:

  ```
  ipfs daemon
  ```

Edit `config.py` and change what's needed.

Run the application:

  ```
  sudo python ipfs-upload.py
  ```
