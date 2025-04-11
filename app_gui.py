from tkinter import *
import customtkinter
import sqlite3
import json
import eTraffic
from eTraffic import Router
from RawProcessing import Gui_help_info_router
from RawProcessing import Utils



# Creating the database




app = customtkinter.CTk()
app.geometry("800x600")
app.title("eTraffic")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


greeting = customtkinter.CTkLabel(app, text="Welcome,Andrew to eTraffic App")
greeting.grid(row=0, column=2, padx=20, pady=20)
select_greeting = customtkinter.CTkLabel(app, text="Select a router or switch,please !")
select_greeting.grid(row=1, column=2, padx=20, pady=20)

def routers():
    path = "../eTrafficApp/router_database.json"
    with open(path,"r") as logging:
        data = json.load(logging)
        routers = data["user_routers"]
        # We will use this to display the routers in the GUI
        routers_list = [] 
        for router in routers:
            routers_list.append(router["router_name"])
        
        print(routers_list)
    #Now find a way to show the routers #TODO
    new_window = customtkinter.CTk()
    new_window.title("Routers Menu")
    new_window.geometry("800x600")
    def optionmenu_callback(choice):
        choice = label.get()
        if len(choice) > 0:
            help_tool = Gui_help_info_router(file_path="../eTrafficApp/router_database.json",choice=choice)
            host_ip = help_tool.host_ip
            username_login_password = help_tool.password_login
            username_login = help_tool.username_login
            vendor = help_tool.vendor
            #Defining the client from eTraffic Framework (Which is very cool by the way)
            #client = Router(host=host_ip,username=username_login,password=username_login_password,vendor=vendor)
            new_window.destroy()
            new_window_choice = customtkinter.CTk()
            new_window_choice.title(choice + " DashBoard Demo")
            new_window_choice.geometry("800x600")
            greeting = customtkinter.CTkLabel(new_window_choice, text="Hello there what do you want to do with this Router?")
            greeting.grid(row=0, column=2, padx=20, pady=20)
            def callback_option(option):
                output  = """
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.1.1     YES manual up                    up
FastEthernet0/1        unassigned      YES unset  administratively down down
GigabitEthernet0/0     10.0.0.1        YES manual up                    up
Serial0/0/0            172.16.0.1      YES manual up                    up
Vlan1                  192.168.0.1     YES manual up                    up
"""

                option = choice.get()
                d = Utils(output=output)
                def callback_option_interfaces(interface):
                    #TODO
                    print("Showing interfaces")
                    print(interface)
                def callback_option_logs(logs):
                    #TODO
                    print("Showing logs")
                    print(logs)
                def callback_option_routing_protocols(routing_protocol):
                    #TODO
                    print("Showing routing protocols")
                    print(routing_protocol)
                if option == "Manage Interfaces Tasks":
                    #Show the interfaces right down the manage interfaces button
                    interfaces = customtkinter.CTkComboBox(new_window_choice,values=d.interfaces,command=callback_option_interfaces)
                    interfaces.grid(row=2,column=2,pady=20)
                    

                elif option == "Manage Logs":
                    values = ["Show NAT"," Show Routing Protocols","Show running config","Show startup config"]
                    logs = customtkinter.CTkComboBox(new_window_choice,values=values,command=callback_option_logs)
                    logs.grid(row=2,column=2,pady=20)
                    
                    
                elif option == "Manage Routing Protocols":
                    logs = customtkinter.CTkComboBox(new_window_choice,values=["OSPF","EIGRP","RIP"],command=callback_option_routing_protocols)
                    logs.grid(row=2,column=2,pady=20)

        
            #Make 3 buttons one interfaces , routing protocols and logs , one by one so like | | 
            choice = customtkinter.CTkSegmentedButton(new_window_choice,values=["Manage Interfaces Tasks","Manage Logs","Manage Routing Protocols"],command=callback_option)
            choice.grid(row=1,column=2,pady=20,padx=20)
            
        else:
            pass
    label = customtkinter.CTkSegmentedButton(new_window,values=routers_list,command=optionmenu_callback)
    
    label.pack(pady=20)
    new_window.mainloop()
    
def show_routers():
    pass
    #TODO   

def switches():
    pass
#TODO


routers = customtkinter.CTkButton(app,text="Routers",command=routers)
routers.grid(row=2,column=0,pady=10)
switches = customtkinter.CTkButton(app,text="Switches",command=switches)
switches.grid(row=2,column=1,pady=10)




app.mainloop()