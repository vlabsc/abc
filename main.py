#!/usr/bin/python

import sys

print " Hello, World! "
print " + -------------------------------------- +"
print " +                                        +"
print " +         A Custom Port Scanner          +"
print " +                                        +"
print " + -------------------------------------- +"
print " \n\n\n"


sys.stdout.write('> ')
sys.stdout.flush()

command = raw_input()

print 'the entered command is ' + command

icmp = {'64':'Compaq Tru64v5.0 | Foundry | FreeBSD | juniper | Linux | Linux 3.* | MacOS/MacTCP | Netgear FVG318', '128': 
'Windows 98, 98SE | Windows NT 4* | Windows ME | Windows 2000* | Windows Server 2003 | Windows XP | Windows Vista | Windows 7 | Windows Server 2008 | Windows 10',
'255':'AIX 3.2,4.1 | BSD | FreeBSD | HP-UX | Irix | Linux 2.2.14 | Linux 2.4 | NetBSD | OpenBSD | OpenVMS | Solaris | Stratus | SunOS | Ultrix'}

print icmp['255']



