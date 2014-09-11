#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "a command line tool that recursively copies everything in the \
                  current directory to a directory called .myvcs (which should be \
                  created if it doesn't already exist)."



import time, sys, os
import progress_bar, system_operations, metadata

from constants import BACKUP_DIR, CONTEND_DIR, OLD_VERSIONS_DIR



"""
    define the next snapshot number
"""
def next_snapshot(dest):
    # Verify whether snapshot (.b3g) folder exists
    system_operations.creating_dir_tree(dest)

    # get the folders in the backup and solder
    folders = system_operations.create_list_of_folders(dest) or ['0']

    try:
        folders.remove(OLD_VERSIONS_DIR)
    except:
        pass

    folders = map(int, folders)
    lastest_snapshot = max(folders) + 1

    return str(lastest_snapshot)



"""
    copy the current files to the snapshot folder
"""
def copy_files(source, dest):
    # Verify whether workplace folder exists
    if not os.path.exists(source):
        print("There is no working file (set to be '%s'). Try again." %source)
        sys.exit(0)

    # create the folder for the new snapshot
    next_snapshot_number = next_snapshot(dest)
    lastest_snapshot = dest + '/' + next_snapshot_number + '/'
    system_operations.creating_dir_tree(lastest_snapshot)

    # get the the files list from the source (the workplace folder)
    files = system_operations.create_list_of_files(source)

    message = "Creating a snapshot " + next_snapshot_number + "... "
    pb = progress_bar.ProgressBar(message)

    # copy the files to the snapshot folder
    for i,f in enumerate(files):
        pb.calculateAndUpdate(i+1, len(files))
        contend_file = source + '/' + f
        backup_file = lastest_snapshot + f
        system_operations.copying_file(contend_file, backup_file)
        if len(files) < 50: # show some progress bar :)
            time.sleep(0.02)

    print("\nDone!\n")
    # return the snapshot value to be updated in the HEAD
    return next_snapshot_number




"""
    Called from the main program, b3g.py
"""
def main(source, dest, message =""):

    # create the snapshot
    next_snapshot_number = copy_files(source, dest)

    # update the header
    metadata.update_header_snapshot(next_snapshot_number, dest, message)





if __name__ == '__main__':

    print("\n--------------------------------------------------------------")
    print("This is just a module. To run the full program, please type:")
    print("$ ./b3g OPTIONS")
    print("--------------------------------------------------------------\n")

    main(CONTEND_DIR, BACKUP_DIR)
