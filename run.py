import os
import subprocess
import shutil

# -----------------------------
# User Inputs
# -----------------------------
CRD_SSH_Code = input("Enter Google CRD SSH Code: ")
Pin = 123456  # 6-digit PIN for CRD

# -----------------------------
# 1. Update & install dependencies
# -----------------------------
subprocess.run([
    "apt", "update"
])
subprocess.run([
    "apt", "install", "-y",
    "xfce4", "xfce4-terminal", "dbus-x11", "x11vnc", "wget", "curl", "sudo", "python3-pip", "xscreensaver"
])

# -----------------------------
# 2. Install Chrome Remote Desktop
# -----------------------------
subprocess.run(["wget", "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"])
subprocess.run(["dpkg", "-i", "chrome-remote-desktop_current_amd64.deb"])
subprocess.run(["apt", "install", "-f", "-y"])
os.system('bash -c \'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session\'')

# Add root to Chrome Remote Desktop group
subprocess.run(["adduser", "root", "chrome-remote-desktop"])

# -----------------------------
# 3. Install Google Chrome
# -----------------------------
subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
subprocess.run(["dpkg", "-i", "google-chrome-stable_current_amd64.deb"])
subprocess.run(["apt", "install", "-f", "-y"])

# ------------------
