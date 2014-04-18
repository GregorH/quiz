#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  unbenannt.py
#
#  Copyright 2014 Lasse Siemoneit <lts_mail@gmx.de>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#



def main():
	print('Wie heißt das Versionenverwaltungssystem an dem Linus Torvalds mitarbeitet?\n')
	eingabe = raw_input('Bitte beantworten Sie die oben genannte Frage\n\n')
	antwort = 'git'
	if eingabe == antwort:
		print('\nDu kennst dich aus!')
		print('\nToll gemacht!')
	else:
		print('\nLies nochmal nach!')
	return 0

if __name__ == '__main__':
	main()

