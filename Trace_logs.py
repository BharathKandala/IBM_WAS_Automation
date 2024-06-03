import sys
import os

def update_trace_service(node_name, server_name, file_name, max_number_of_backup_files, rollover_size):
    server = AdminConfig.getid('/Node:%s/Server:%s/' % (node_name, server_name))
    traceService = AdminConfig.list('TraceService', server)
    traceLog = AdminConfig.showAttribute(traceService, 'traceLog')
    AdminConfig.show(traceLog)

    # Modify parameters only if they are not empty
    if file_name:
        AdminConfig.modify(traceLog, [['fileName', file_name]])
    if max_number_of_backup_files:
        AdminConfig.modify(traceLog, [['maxNumberOfBackupFiles', max_number_of_backup_files]])
    if rollover_size:
        AdminConfig.modify(traceLog, [['rolloverSize', rollover_size]])

    AdminConfig.save()
    print("TraceService Configuration updated successfully.")

# Extracting command line arguments
node_name = sys.argv[0]
server_name = sys.argv[1]
file_name = sys.argv[2] if sys.argv[2] != "EMPTY" else ""
max_number_of_backup_files = int(sys.argv[3]) if sys.argv[3] != "EMPTY" else None
rollover_size = int(sys.argv[4]) if sys.argv[4] != "EMPTY" else None

update_trace_service(node_name, server_name, file_name, max_number_of_backup_files, rollover_size)


#sh wsadmin.sh -lang jython -f file1.py sc-q-autwas02DmgrNode dmgr ${LOG_ROOT}/dmgr/trace.logss EMPTY 65