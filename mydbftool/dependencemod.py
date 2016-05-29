#!/usr/bin/env python3
import os
import subprocess

pip = '/usr/bin/pip'
pip3 = '/usr/bin/pip3'
sudo = '/usr/lib/sudo'
lsb =  '/usr/bin/lsb_release'
ln = '/bin/ln'
dpkg = '/usr/bin/dpkg'


def debiancheck():
    """Debian check"""
    debwork =  subprocess.Popen([lsb,'-d'], stdout = subprocess.PIPE)
    deblist = debwork.communicate()
    if str(deblist).find('Debian') >= 0:
        return 1
    else:
        os.sys.exit()


def mysqlconnectorcheck():
    """Check install python3-mysql.connector"""
    dpkgwork = subprocess.Popen([dpkg,'-s', 'python3-mysql.connector'],stdout = subprocess.PIPE)
    dpkglist = dpkgwork.communicate()
    for i in dpkglist:
        if str(dpkglist).find('Status: install ok installed') < 0:
            print('to use mysql want package python3-mysql.connector')
            return 0
        else:
            return 1


def simpledbfcheck():
    """Check install simpledbf"""
    pipwork =  subprocess.Popen([pip, 'list'], stdout = subprocess.PIPE)
    piplist = pipwork.communicate()
    if str(piplist).find('simpledbf') >= 0:
        return 1


def dbfcheck():
    """Check install dbf"""
    pipwork =  subprocess.Popen([pip3, 'list'], stdout = subprocess.PIPE)
    piplist = pipwork.communicate()
    if str(piplist).find('dbf (') >= 0:
        return 1


def simpledbfinstall():
    """Pip install simple dbf"""
    if debiancheck() == 0:
        print('Dependence check not work if the os not  Debian')
        os.sys.exit()
    if mysqlconnectorcheck() == 0:
        os.sys.exit()
    if '/usr/lib/python3/dist-packages' in os.sys.path:
        libpath3 = '/usr/lib/python3/dist-packages/simpledbf'
        libpath2 = '/usr/lib/python3/dist-packages/simpledbf'
    working = subprocess.Popen([sudo, pip,'install simpledbf'])
    move = subprocess.Popen([sudo,ln,'-sr', libpath2, libpath3])
    return 1


def install():
    if simpledbfcheck() == 1:
        print('simpledbf уже есть в системе')
        open('install.chk','w').write('1')
    else:
       simpledbfinstall()
       open('install.chk','w').write('1')