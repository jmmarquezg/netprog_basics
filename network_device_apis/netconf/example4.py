#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Device APIs
Lesson: Goodbye SNMP hello NETCONF

example4.py
Illustrate the following concepts:
- Send <get> to retrieve config and state data
- Process and leverage XML within Python
- Report back current state of interface
- Create new file to store reply
- Function definition to perform all the tasks
"""

__author__ = "Jose Marquez"
__author_email__ = "jmarque2@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import xmltodict
from ncclient import manager
from device_info import ios_xe1
from pprint import pprint

# Creando el filtro que nos dara la informacion de la interfaz que buscamos. En este caso Loopback 11
filter = open("filter-ietf-interfaces-2.xml").read()

def get_int_info():
    with manager.connect(host = ios_xe1["address"],
                        port = ios_xe1["port"],
                        username = ios_xe1["username"],
                        password = ios_xe1["password"],
                        hostkey_verify = False) as m:

                        reply = m.get(filter)
    
    loop_file = "loop_int.xml"
    with open(loop_file, "w") as f:
        f.write(reply.xml)
    
    int_params = xmltodict.parse(reply.xml)["rpc-reply"]["data"]["interfaces"]["interface"]
    int_stats = xmltodict.parse(reply.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]
    
    print("LOS DATOS DE LA INTERFAZ SON:\n")
    print("NOMBRE: {}".format(int_params["name"]["#text"]))
    print("DESCRIPCION: {}".format(int_params["description"]))
    print("IP ADDRESS: {}".format(int_params["ipv4"]["address"]["ip"]))
    print("ADMIN STATUS: {}".format(int_stats["admin-status"]))
    print("OPER STATUS: {}".format(int_stats["oper-status"]))
    print("TIEMPO: {}".format(int_stats["statistics"]["discontinuity-time"]))

if __name__ == '__main__':
    get_int_info()