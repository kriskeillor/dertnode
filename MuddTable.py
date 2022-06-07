# Kris Keillor
# Table (CSV) Script
# Multi User Data Daemon (MUDD) library
# v0.5.0
# Prof. Junaid Khan
# EECE 397A Wireless Networking
#   *   *   *   *   *   *


#   *   *   *   *   *   *
# INCLUDES
#   *   *   *   *   *   *
# System module
import sys
# Local Library Files
try:
    from ERROR_CODES import PICO_ERROR_NONE as ERR_NONE
    from ERROR_CODES import PICO_ERROR_TIMEOUT as ERR_TIMEOUT
    from ERROR_CODES import PICO_ERROR_GENERIC as ERR_GENERIC
    from ERROR_CODES import PICO_ERROR_NO_DATA as ERR_NO_DATA
except ImportError:
    print("Error loading FTD library file ERROR_CODES.py.")
    sys.exit(-1)
# Modules
import os
import sys
import traceback
try:
    from datetime import datetime
except ImportError:
    print("Datetime module import failed")
    sys.exit(ERR_GENERIC)
try:
    import csv
except ImportError:
    print("CSV module import failed")
    sys.exit(ERR_GENERIC)
#   *   *   *   *   *   *


#   *   *   *   *   *   *
# DATA FUNCTIONS
#   *   *   *   *   *   *
# Bulk add-value to all rows
def append_values_bulk(fname_in, col_add, fname_out):
    data_out = []
    # Open input
    filestream_in = open_reader_stream(fname_in)
    with filestream_in:
        reader = csv.reader(filestream_in)
        headers = next(reader)
        data_out = [headers] + [row + [col_add] for i, row in enumerate(reader)]
    filestream_in.close()
    # Open output
    filestream_out = open_writer_stream(fname_out)
    with filestream_out:
        csv.writer(filestream_out, delimiter=",").writerows(data_out)
    filestream_out.close()
    return ERR_NONE

# Append a single name-value pair, automatically generating timestamp
def append_entry(fname_in, val_name, value):
    data_out = []
    # Open input
    filestream_in = open_append_stream(fname_in)
    with filestream_in:
        writer = csv.writer(filestream_in)
        writer.writerow([val_name, value, datetime.now()])
    filestream_in.close()
    return ERR_NONE

# Get rows that correspond to a certain DataCode and write to a file
def get_rows_by_code(fname_in, code, fname_out):
    data_out = []
    # Open input
    with open(fname_in, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            if row[0] in code:
                data_out += row
    filestream_out = open_writer_stream(fname_out)
    with filestream_out:
        csv.writer(filestream_out, delimiter=",").writerows(data_out)
    filestream_out.close()
    return ERR_NONE

#   *   *   *   *   *   *
# FILE SYSTEM FUNCTIONS
#   *   *   *   *   *   *
# Read object
def open_reader_stream(fname):
    try:
        reader_str = open(fname, "rt", newline='')   # Open in "read text" mode
        return reader_str
    except:
        print("Could not read file " + fname)
        sys.exit(ERR_NO_DATA)
# Write object
def open_writer_stream(fname):
    try:
        writer_str = open(fname, "wt", newline='\n')   # Open in "write text" mode
        return writer_str
    except Exception:
        print(traceback.format_exc())
        print("Could not write file {}".format(fname))
        sys.exit(ERR_NO_DATA)
# Append object
def open_append_stream(fname):
    try:
        append_str = open(fname, "at", newline='\n')   # Open in "append text" mode
        return append_str
    except:
        print(fname)
        print("Could not append file {}".format(fname))
        sys.exit(ERR_NO_DATA)
# Print a CSV table
def print_stream(fname):
    #reader_str
    try:
        reader_str = open(fname, "rt", newline='\n')
    except:
        print("Could not open file {}".format(fname))
        return ERR_NO_DATA
    with (reader_str):
        row = next(reader_str, None)
        while row is not None:
            print(row)
            row = next(reader_str, None)
    return ERR_NONE
