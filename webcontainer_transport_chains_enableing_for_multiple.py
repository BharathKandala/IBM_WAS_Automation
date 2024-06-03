# Importing necessary packages
import sys
import os

# Function to enable/disable web container transport chains
def webcontainer_transport_chains_enableing(server_name, enable_value, chain_names):
    # Get the Server ID
    server_id = AdminConfig.getid('/Server:%s' % server_name)
    # List all TransportChannelServices for the server
    TCS = AdminConfig.list("TransportChannelService", server_id)
    # List all transport chains in the TransportChannelService
    chains = AdminTask.listChains(TCS).splitlines()

    # Iterate through the chains and enable/disable the specified transport chains
    for chain in chains:
        for chain_name in chain_names:
            if chain_name in chain:
                
                AdminConfig.modify(chain, [['enable', enable_value]])

    # Save changes
    AdminConfig.save()
    print("Webcontainer transport chains configuration updated successfully.")

# Extracting command line arguments
server_name = sys.argv[0]
enable_value = sys.argv[1]
chain_names = sys.argv[2].split(",") if sys.argv[2] != "EMPTY" else []

# Call function to enable/disable web container transport chains
webcontainer_transport_chains_enableing(server_name, enable_value, chain_names)

#sh wsadmin.sh -lang jython -f file1.py 'servera' true 'HttpQueueInboundDefault(','WCInboundDefault('
