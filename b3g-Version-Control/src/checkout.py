#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"
__description__= "Revert to an earlier snapshot."


import sys
import os
import hashlib
import time

import progress_bar, system_operations, metadata
from constants import BACKUP_DIR, OLD_VERSIONS_DIR, CONTEND_DIR




"""
    copy the backup folder to the work folder
"""
def do_moving(workfolder, checkoutfolder):

    # get the files from the snapshot
    files = system_operations.create_list_of_files(checkoutfolder)
    pb = progress_bar.ProgressBar("Checking out " + checkoutfolder + "...")


    # TODOl cleaning working directory, so we get the snapshot right
    # TODO: this must die!!! use the diff function
    system_operations.moving_dir(workfolder + "/" + BACKUP_DIR, BACKUP_DIR)
    system_operations.removing_dir_tree(workfolder)
    system_operations.creating_dir_tree(workfolder)
    system_operations.moving_dir(BACKUP_DIR, workfolder)


    # copying the snapshot to the work folder
    for i, file in enumerate(files):
        pb.calculateAndUpdate(i + 1, len(files))
        backup_file = checkoutfolder + '/' + file
        system_operations.copying_file(backup_file, workfolder)
        time.sleep(0.02)




"""
    After checking out we don't need anything made after the
    snapshot you are going to. So we move this to a deprecated folder
"""
def move_deprecate_folders(dest, co_folder):

    # get the deprecated folders
    folders = system_operations.create_list_of_folders(dest)
    try:
        folders.remove(OLD_VERSIONS_DIR)
    except:
        pass

    folders = [str(f) for f in map(int, folders) if f > int(co_folder)]
    folder_id = 0

    # create a deprecated folder
    if folders:
        # create a unique hash file
        folder_id = hashlib.sha1()
        folder_id.update(str(time.time()))
        folder_id = folder_id.hexdigest()[:15]

        deprecated_folder = dest + '/' + OLD_VERSIONS_DIR + "/" + folder_id
        system_operations.creating_dir_tree(deprecated_folder)

        # move deprecated folders
        for folder in folders:
            source_folder = dest + "/" + folder
            dest_folder = deprecated_folder + '/' + folder
            system_operations.moving_dir(source_folder, dest_folder)

    return folder_id



"""
    find the last snapshot number
"""
def get_snapshot(source, argument):

    # Verify whether destination folder(.b3g) exists
    if not os.path.exists(source):
        print("Not possible to checkout. You do not have any snapshot yet.")
        sys.exit(0)

    # now check the argument
    if argument == 'latest' or argument == 'l':
        folders = system_operations.create_list_of_folders(source)
        folders = map(int, folders)
        return source + '/' + str(max(folders))

    path = source + '/' + argument

    try:
        assert(int(argument) > 0)
    except:
        print("Argument is not valid.")
        sys.exit(0)

    try:
        assert(os.path.exists(path))
    except:
        print("Snapshot %s does not exist or is not a valid value." %argument)
        sys.exit(0)

    return path



"""
    In the main function we verify the arguments and if the \
    asked folders exists. Then we copy the snapshot and update \
    the HEAD.
"""
def main(dest, source, co_folder):
    # find the path to the folder we are checking out
    # dest is workplace/.b3g
    # source is workplace
    # path gets the entire path to the co_folder
    path = get_snapshot(dest, co_folder)

    # move the folders we don't want to the deprecated folder
    folder_id = move_deprecate_folders(dest, co_folder)

    # make header for the deprecated folder, if a folder was created
    if folder_id:
        metadata.update_header_checkout(dest, co_folder, folder_id)

    # do the checkout to the workplace folder
    do_moving(source, path)





if __name__ == '__main__':

    print("\n--------------------------------------------------------------")
    print("This is just a module. To run the full program, please type:")
    print("$ ./b3g OPTIONS")
    print("--------------------------------------------------------------\n")


    main(CONTEND_DIR, BACKUP_DIR, argument='2')
