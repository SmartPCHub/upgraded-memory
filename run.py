import os
import subprocess
import shutil

# --- User Inputs ---
CRD_SSH_Code = input("Enter Google CRD SSH Code: ")
Pin = 123456  # 6-digit pin for CRD

# --- 1. Update & install dependencies ---
os.system("apt update && apt install -y xfce4 xfce4-terminal dbus-x11 x11vnc wget curl sudo python3-pip")

# --- 2. Install Chrome Remote Desktop ---
os.system("wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb")
os.system("dpkg -i chrome-remote-desktop_current_amd64.deb")
os.system("apt i
