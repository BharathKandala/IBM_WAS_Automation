# Function to create Application Server
def create_application_server(server_name, node_name):
    nodeAgent = AdminControl.queryNames('type=NodeAgent,node=' + node_name + ',process=nodeagent,*')
    server = AdminTask.createApplicationServer(node_name, '-name ' + server_name + ' -templateName default')
    AdminConfig.save()
    print("Server '%s' created successfully on node '%s'" % (server_name, node_name))

def load_endpoint_ports(file_path):
    endpoint_ports = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                endpoint_ports[key] = value
    return endpoint_ports

def modify_server_ports(server_name, node_name, file_path):
    node = AdminConfig.getid('/Node:' + node_name + '/')
    serverEntries = AdminConfig.list('ServerEntry', node).split(java.lang.System.getProperty('line.separator'))

    # Load endpoint ports from file
    endpoint_ports = load_endpoint_ports(file_path)

    for serverEntry in serverEntries:
        sName = AdminConfig.showAttribute(serverEntry, "serverName")
        if sName == server_name:
            sepString = AdminConfig.showAttribute(serverEntry, "specialEndpoints")
            sepList = sepString[1:len(sepString)-1].split(" ")
            for specialEndPoint in sepList:
                endPointNm = AdminConfig.showAttribute(specialEndPoint, "endPointName")
                if endPointNm in endpoint_ports:
                    ePoint = AdminConfig.showAttribute(specialEndPoint, "endPoint")
                    port_number = endpoint_ports[endPointNm]
                    AdminConfig.modify(ePoint, [["port", port_number]])
    AdminConfig.save()

# Example usage
server_name = 'serverX'
node_name = "sc-q-autwas03Node"
file_path = 'path/to/endpoint_ports.txt'

modify_server_ports(server_name, node_name, file_path)
