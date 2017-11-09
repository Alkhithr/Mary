# In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.
#
# Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
#
# To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two files have the same checksum, they probably have the same contents.
#
# To double-check, you can use the Unix command diff.
import os
import dbm
import pickle

# file_db = 'files_db'


def find_dups(dir):

    # if os.path.exists(file_db):
    #     os.remove(file_db)

    walk_list = os.walk(dir, topdown=True, onerror=None, followlinks=False)

    # dbout = dbm.open(file_db, 'n')

    file_db = dict()

    for line in walk_list:

        directory = line[0]
        files = line[2]

        for file in files:
            if file_db.get(file) is None:
                file_db[file] = [1, [directory]]
            else:
                instances = file_db[file][0] + 1
                directories = [directory] + file_db[file][1]
                file_db[file] = [instances, directories]

    for item in file_db:
        if file_db[item][0] > 10:
            print(item, file_db[item][0])


find_dups('/Users/antonio/Downloads/')
