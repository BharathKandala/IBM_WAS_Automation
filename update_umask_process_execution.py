import sys
import os


def update_umask_process_execution(node_name, server_name, process_Priority, runAs_Group, runAs_User, runIn_ProcessGroup, umask_value):
    server = AdminConfig.getid('/Node:%s/Server:%s/' % (node_name, server_name))

    processExecution = AdminConfig.list('ProcessExecution', server)

    # Modify parameters only if they are not empty
    if process_Priority:
        AdminConfig.modify(processExecution, [['processPriority', process_Priority]])

    if runAs_Group:
        AdminConfig.modify(processExecution, [['runAsGroup', runAs_Group]])
    if runAs_User:
        AdminConfig.modify(processExecution, [['runAsUser', runAs_User]])
    
    if runIn_ProcessGroup:
        AdminConfig.modify(processExecution, [['runInProcessGroup', runIn_ProcessGroup]])

    if umask_value:
        AdminConfig.modify(processExecution, [['umask', umask_value]])

    AdminConfig.save()
    print("Umask process execution Configuration updated successfully.")

# Extracting command line arguments
node_name = sys.argv[0]
server_name = sys.argv[1]
process_Priority = sys.argv[2] if sys.argv[2] != "EMPTY" else None
runAs_Group = int(sys.argv[3]) if sys.argv[3] != "EMPTY" else ""
runAs_User = int(sys.argv[4]) if sys.argv[4] != "EMPTY" else ""
runIn_ProcessGroup = int(sys.argv[5]) if sys.argv[5] != "EMPTY" else None
umask_value  = int(sys.argv[6]) if sys.argv[6] != "EMPTY" else None

update_umask_process_execution(node_name, server_name, process_Priority, runAs_Group, runAs_User, runIn_ProcessGroup, umask_value)

#execution command

#sh wsadmin.sh -lang jython -f file1.py sc-q-autwas02DmgrNode dmgr EMPTY EMPTY EMPTY 1 025