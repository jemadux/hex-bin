#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  hexadecimal-bin.py
#  
#  Copyright 2013 Klearchos-Angelos Gkountras <kleagkou@gmail.com>
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
numb=num=input("Give the number to make it on binary and hexadecimal ")

binary = list()
while num >= 1:
  binary.insert(0, num % 2)
	num /= 2 
print binary
	
hexadecimal = list()
digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while numb >= 1:
	remain = numb % 16
	hexadecimal.insert(0, digits[remain])
	numb /= 16
print hexadecimal
