#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Ramazan"
echo "Surname: Suleimanov"
echo "Group: IT2-2308"
echo "Student ID: 37408"

echo "=============================="
echo "System Information"
echo "=============================="
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s)"
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
free -h

echo "=============================="
if [ -f "Suleimanov_Ramazan_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
