import re
import json

class Utils():
    def __init__(self,output:str):
        self.output = output
        #Doing the interfaces IP
        self.interfaces = []
        interfaces_pattern = r'([A-Za-z]+[0-9]+/[0-9]+)'
        interfaces_regex = re.findall(interfaces_pattern, output)
        for interface in interfaces_regex:
            self.interfaces.append(interface)
    
    #This is for the GUI specfically
class Gui_help_info_router():
    def __init__(self,file_path,choice:str):
         self.file_path = file_path
         self.choice = choice
         with open(file_path,"r") as logging:
            data = json.load(logging)
            routers = data["user_routers"]
            for item in routers:
                if item["router_name"] == choice:
                    self.username_login = item["username_login"]
                    self.host_ip = item["host_ip"]
                    self.password_login = item["password_login"]
                    self.vendor = item["Vendor"]
        
    
        




