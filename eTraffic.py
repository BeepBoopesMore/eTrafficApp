import paramiko
import json
import os
import socket
from RawProcessing import  Utils





class Router():
    def __init__(self,username:str,password:str,host:str,vendor:str):
        self.username = username
        self.password = password
        self.host = host
        self.vendor = vendor
        if self.vendor.lower() == "cisco":
            #Commands for cisco
            #Interfaces
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,username=self.username,password=self.password)
            command_interfaces = "enable && show ip interface brief"
            stdin, stdout, stderr = client.exec_command(command_interfaces)
            output_interfaces = stdout.read().decode()
            self.interfaces = Utils(output=output_interfaces).interfaces
            #Do here to check if the router is down
            #TODO
            #!!!



        elif self.vendor.lower() == "juniper":
            pass
        #TODO
        else:
            #TODO
            pass










