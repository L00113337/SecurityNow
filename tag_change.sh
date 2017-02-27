#!/bin/bash

# Author: Mateusz Sobczak aka Brains
# Date: 26/08/2016
# Desc: This script will change mp3 tags of all the episodes.

clear
clear
echo ------------------------------------------------------------
cover_loc=$(pwd)
cover_loc="$cover_loc/cover.jpg"
location=$(grep -o "save_directory = '[^']*'" sn-dwnldr.py | grep -o "/[^']*/")
echo "location of audio files: " $location
echo -n "Changing to that location..."
cd $location
echo "Done"
echo ------------------------------------------------------------
echo -n "Deleting all tags..."
mid3v2 -D *
echo "Done"
echo ------------------------------------------------------------
echo -n "Setting Author, Genre, Cover tags to all files..."
mid3v2 --TPE1 "Steve Gibson with Leo Laporte" --TCON "Podcast" --APIC $cover_loc *
echo "Done"
echo ------------------------------------------------------------
echo "Setting Album tags:"
echo ------------------------------------------------------------
echo -e "\t(Security Now 2005)"
for i in {1..9}
do
	echo -en "\t\tsn000$i.mp3..."
	mid3v2 --TALB "Security Now 2005" sn000$i.mp3
	mid3v2 --TIT2 "Security Now Episode #000$i" sn000$i.mp3
	echo "Done"
done
for i in {10..20}
do
	echo -en "\t\tsn00$i.mp3..."
	mid3v2 --TALB "Security Now 2005" sn00$i.mp3
	mid3v2 --TIT2 "Security Now Episode #00$i" sn00$i.mp3
	echo "Done"
done	
echo ------------------------------------------------------------
echo -e "\t(Security Now 2006)"
for i in {21..72}
do
	echo -en "\t\tsn00$i.mp3..."
	mid3v2 --TALB "Security Now 2006" sn00$i.mp3
	mid3v2 --TIT2 "Security Now Episode #00$i" sn00$i.mp3
	echo "Done"
done
echo ------------------------------------------------------------
echo -e "\t(Security Now 2007)"
for i in {73..99}
do
	echo -en "\t\tsn00$i.mp3..."
	mid3v2 --TALB "Security Now 2007" sn00$i.mp3
	mid3v2 --TIT2 "Security Now Episode #00$i" sn00$i.mp3
	echo "Done"
done
for i in {100..124}
do
	echo -en "\t\tsn0$i.mp3..."
	mid3v2 --TALB "Security Now 2007" sn0$i.mp3
	mid3v2 --TIT2 "Security Now Episode #0$i" sn0$i.mp3
	echo "Done"
done
echo ------------------------------------------------------------
echo -e "\t(Security Now 2008)"
for i in {125..176}
do
	echo -en "\t\tsn0$i.mp3..."
	mid3v2 --TALB "Security Now 2008" sn0$i.mp3
	mid3v2 --TIT2 "Security Now Episode #0$i" sn0$i.mp3
	echo "Done"
done
