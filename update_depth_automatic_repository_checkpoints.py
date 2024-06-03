import sys
import os

def update_depth_automatic_repository_checkpoints(auto_Checkpoints_Depth, auto_checkpoints_enabled, checkpoint_Root):
    ers_service = AdminConfig.getid('/ExtendedRepositoryService:/')

    # Modify parameters only if they are not empty
    if auto_Checkpoints_Depth:
        AdminConfig.modify(ers_service, [['autoCheckpointsDepth', auto_Checkpoints_Depth]])
    if auto_checkpoints_enabled:
        AdminConfig.modify(ers_service, [['autoCheckpointsEnabled', auto_checkpoints_enabled]])
    if checkpoint_Root:
        AdminConfig.modify(ers_service, [['checkpointRoot', checkpoint_Root]])

    AdminConfig.save()
    print("Depth automatic repository checkpoints Configuration updated successfully.")

# Extracting command line arguments
auto_Checkpoints_Depth = sys.argv[0] if sys.argv[0] != "EMPTY" else None
auto_checkpoints_enabled = sys.argv[1] if sys.argv[1] != "EMPTY" else ""
checkpoint_Root = sys.argv[2] if sys.argv[2] != "EMPTY" else ""

update_depth_automatic_repository_checkpoints(auto_Checkpoints_Depth, auto_checkpoints_enabled, checkpoint_Root)


# sh wsadmin.sh -lang jython -f file1.py 5 true '${USER_INSTALL_ROOT}/checkpoints'