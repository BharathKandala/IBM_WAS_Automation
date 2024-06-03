import sys
import os

def create_web_containers_under_custom_properties(cs_name, cs_value, cs_description, server_name):

    serverId = AdminConfig.getid('/Server:' + server_name + '/' )
    serverWebContainer = AdminConfig.list("WebContainer", serverId )

    attrs = [["name", cs_name], ["value", cs_value], ["description", cs_description]]

    AdminConfig.create("Property", serverWebContainer, attrs )

    AdminConfig.save()
    print("create web containers under custom properties Configuration updated successfully.")

# Extracting command line arguments
cs_name = sys.argv[0] if sys.argv[0] != "EMPTY" else ""
cs_value = sys.argv[1] if sys.argv[1] != "EMPTY" else ""
cs_description = sys.argv[2] if sys.argv[2] != "EMPTY" else ""
server_name = sys.argv[3]

create_web_containers_under_custom_properties(cs_name, cs_value, cs_description,server_name)


#  sh wsadmin.sh -lang jython -f file1.py 'com.ibm.ws.webcontainer.channelwritetype' 'sync' 'test' 'servera'
# sh wsadmin.sh -lang jython -f file1.py 'com.ibm.ws.webcontainer.channelwritetype' 'sync' EMPTY 'servera'