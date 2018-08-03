# !/usr/bin/python2.7 
# -*- coding: utf-8 -*- 
# 获取集成显卡名称
# author: tongyang

import _winreg

key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Enum\PCI")

child_count = _winreg.QueryInfoKey(key)[0]

keylist = []

for i in range(int(child_count)):
    child = _winreg.EnumKey(key, i)
    child_key = _winreg.OpenKey(key, child)
    child2 = _winreg.EnumKey(child_key, 0)
    child2_key = _winreg.OpenKey(child_key, child2)
    try:
        service_value = _winreg.QueryValueEx(child2_key, "Service")
    except WindowsError:
        continue
    if service_value[0] == u'igfx':
        device_desc_value = _winreg.QueryValueEx(child2_key, 'DeviceDesc')
        print(device_desc_value[0])
		
_winreg.CloseKey(key)