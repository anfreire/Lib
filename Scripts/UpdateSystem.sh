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
		sudo apt update -y
		sudo apt upgrade -y
		sudo apt full-upgrade -y
		sudo apt dist-upgrade -y
		sudo apt autoclean -y
		sudo apt clean -y
		sudo apt autoremove -y
	elif [ $package == $APTITUDE ]; then
		sudo aptitude install -f -y
		sudo aptitude update -y
		sudo aptitude upgrade -y
		sudo aptitude full-upgrade -y
		sudo aptitude dist-upgrade -y
		sudo aptitude autoclean -y
		sudo aptitude clean -y
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




