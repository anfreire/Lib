#!/bin/bash

APT="apt"
APTITUDE="aptitude"

function update_system () {
	local package=$1
	sudo dpkg --configure -a
	flatpak uninstall --unused
	flatpak update
	if [ $package == $APT ]; then
		sudo apt install -f -y
		sudo apt update 
		sudo apt upgrade 
		sudo apt full-upgrade 
		sudo apt dist-upgrade 
		sudo apt autoclean 
		sudo apt clean 
		sudo apt autoremove 
	elif [ $package == $APTITUDE ]; then
		sudo aptitude install -f -y
		sudo aptitude update 
		sudo aptitude upgrade 
		sudo aptitude full-upgrade 
		sudo aptitude dist-upgrade 
		sudo aptitude autoclean 
		sudo aptitude clean 
	fi
}


echo "Which package manager do you want to use?"
echo "1) apt"
echo "2) aptitude"
read -p "Enter your choice: " choice
case $choice in
	1) update_system $APT;;
	2) update_system $APTITUDE;;
	*) echo "Invalid choice";;
esac




