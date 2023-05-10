#!/bin/sh

if [[ $(arch) == 'i386' ]]; then
  	echo Intel Mac
	IDIR="/usr/local/include"
	LDIR="/usr/local/lib"
	NCL="-lncurses"
elif [[ $(arch) == 'arm64' ]]; then
  	echo M1 Mac
	IDIR="/opt/homebrew/include"
	LDIR="/opt/homebrew/lib"
	NCL="-lncurses"
else
	echo Win PC
	IDIR="/mingw64/include"
	LDIR="/mingw64/lib"
	NCL=
fi

gcc -Wall -o synth main.c user_io.c synth.c paUtils.c \
	-I$IDIR -L$LDIR -lsndfile -lportaudio $NCL
