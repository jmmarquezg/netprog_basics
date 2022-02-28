#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Device APIs
Lesson: Goodbye SNMP hello NETCONF
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- Opening a NETCONF connection with ncclient
- Saying <hello> and review capabilities
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from device_info import ios_xe_latest
from ncclient import manager

if __name__ == '__main__':
    with manager.connect(host=ios_xe_latest["address"], port=ios_xe_latest["port"],
                         username=ios_xe_latest["username"],
                         password=ios_xe_latest["password"],
                         hostkey_verify=False) as m:

        print("Here are the NETCONF Capabilities")
        print(type(m))
        for capability in m.server_capabilities:
            print(capability)
