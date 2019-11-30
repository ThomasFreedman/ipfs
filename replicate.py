#!/usr/bin/python3

#
# Program to replicate an IPFS server populated with
# ytdl-ipfs????.py
#
# This requires the SQLite3 database from the servers
# being replicated. It simply does an "ipfs cat <has>"
# for every hash in the database, then does an "ipfs
# add file" obtained. This results in a different hash
# for the same content!!!
#
from __future__ import unicode_literals
from datetime import *
import sqlite3
import sys
import os

HOME   = os.path.dirname(os.path.realpath(__file__)) + '/'

# GLOBALS
OpCounter     = 0    # Count of IPFS operations done


def usage():
    print("\nReplicate files on a remote IPFS server on local IPFS server.")
    print("Requires Sqlite3 database file that specifies the files.\n")
    print("Usage: %s <-db file> | <--database file>\n" % sys.argv[0])
    print("The ipfs command must be in the $PATH")
    print("To view progress and create a log file use:")
    print("%s <args> | tee <log file name>" % sys.argv[0])
    exit(0)


# Prints IPFS operations done and day / time marker on console
def printMarker(newLine=False):
    global OpCounter
    now = datetime.now()
    str = "Ops: %5d %s"
    if newLine: str += "\n"
    mark = str % (OpCounter, now.strftime("%a %H:%M:%S"))
    print(mark, flush=True)
    OpCounter = OpCounter + 1


# Copy video & meta files from remote node into local virtual folder & pin them
# Print progress as IPFS operations counter with day and time
def copyPinFiles(row):
    grupe = row[0]
    vhash = row[1]
    mhash = row[2]
    video = os.path.basename(str(row[3]))
    meta  = video.split(".")[0] + ".info.json"

    printMarker(True)
    copyCmd = "ipfs files cp /ipfs/" + vhash + " /" + grupe + "/" + video
    os.system("echo " + copyCmd)
#    os.system(copyCmd)

    printMarker()
    pinCmd = "ipfs pin add --progress --recursive=true /ipfs/" + vhash
    os.system("echo " + pinCmd + "\n")
#    os.system(pinCmd + "\n")

    printMarker(True)
    copyCmd = "ipfs files cp /ipfs/" + mhash + " /" + grupe + "/" + meta
    os.system("echo " + copyCmd)
#    os.system(copyCmd)

    printMarker()
    pinCmd = "ipfs pin add --progress --recursive=true /ipfs/" + mhash
    os.system("echo " + pinCmd + "\n")
#    os.system(pinCmd + "\n")




#############################################################################
#                                                                           #
# The main loop                                                             #
#                                                                           #
#############################################################################
argc = len(sys.argv)
conn = errors = grupe = sql = False

try:
    # Parse command line
    if argc > 1:
        if argc > 2 and (sys.argv[1] == "-db" or sys.argv[1] == "--database"):
            dbFile = sys.argv[2]
            conn = sqlite3.connect(dbFile)
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            usage()
    else: usage()

    conn.row_factory = sqlite3.Row   # Set query results to dictionary format
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM IPFS_HASH_INDEX")
    rowCount = int(cursor.fetchone()[0])
    print("Database currently has %d rows\n" % rowCount)

    # Primary loop to obtain the files we'll replicate locally
    sql = "SELECT grupe,mhash,vhash,_filename FROM IPFS_HASH_INDEX order by grupe"
    for row in cursor.execute(sql):
        if row[0] != grupe:
            grupe = row[0]
            os.system("echo 'ipfs files mkdir /" + grupe + "'")
#            os.system("ipfs files mkdir /" + grupe)

        # Process this row into IPFS
        copyPinFiles(row)


except sqlite3.Error as e:
    print("Database error during query: %s\nSQL=%s\n\n" % (e, sql))

except Exception as e:
    print("Exception in query: %s\nSQL=%s\n\n" % (e, sql))

except sqlite3.OperationalError:
    print("ERROR!: Query Failure")

exit(0)
