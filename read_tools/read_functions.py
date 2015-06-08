
#
# Copyright William Martin 2015
# GPL2
# wgm2111 at columbia dot edu 

"""
Module with some routines for reading in some SHDOM files from Frank Evans.

In general, I want the read routines to return

*IN*
filename  : a data file

*OUT* 
comments : A string of comment lines
data_frame : a data frame object

"""

from __future__ import print_function, division

import os.path, time
 
import pandas



# Define a function to read only the comments
# --
def read_comments(filename, comment="!"):
    """
    Read the comment lines and stop after encountering five consecutive
    non-comment lines. 
    """

    # Function behavior
    non_comment_max = 5         # terminate after this many lines
    non_comment_counter = 0     # initialized counter

    # Open the file and read lines
    with open(filename) as ofile:
        
        # loop and store comments, break after encountering non-comment lines
        reading_comments = True
        comment_lines = []

        # Keep reading lines until the comment counter is greater than the max
        while non_comment_counter <= non_comment_max:

            # The next line
            line = ofile.readline().strip()

            # Cases 
            if len(line)==0:    # empty line
                non_comment_counter += 1
                comment_lines.append("")

            elif line[0] == "!": # comment line
                non_comment_counter = 0 # reset the counter
                comment_lines.append(line)

            else:               # non-comment non-empty
                non_comment_counter += 1
                comment_lines.append(line)

        # Make a string of comments
        comments = '\n'.join(comment_lines[:-(non_comment_max+1)])

        # Return the list of comment lines
        return comments


# Define a funtion that reads comments and then makes a tab separated data_file
def _make_file_for_readcsv(filename):
    """
    Make a new file with filename.  filename+"_for_readcsv"
    """
    # New filename
    filename_for_readcsv = filename + "_for_readcsv"

    # Read the comments
    comments = read_comments(filename)
    comment_lines = comments.split('\n')

    # Get the last comment line
    Nlines = len(comment_lines)
    header_line = comment_lines[-1]

    # Open the file to read
    with open(filename, 'r') as fold:
        with open(filename_for_readcsv, 'w') as fnew:
            
            # Read through the header
            nline = 0
            while nline <= Nlines: 
                nline+=1
                fold.readline()
                pass
                
            # Read the first data line and count the number of columns
            first_data_line = fold.readline()
            Ncols = len(first_data_line.strip().split())

            # Save the header to fnew
            fnew.write("  " + "  ".join(header_line.strip().split()[1:(Ncols+1)]) + "\n")
            fnew.write(first_data_line)
            fnew.flush()
            fnew.write(fold.read()) # write the rest of the lines to disk

            # Flush and close the openfiles
            fnew.flush()
            fnew.close()
            fold.close()

    return filename_for_readcsv


    


def read_adj(filename):
    """
    Read a shdome "*.adj" file. 
    """
    # Read file
    comments = read_comments(filename)
    
    # Make a special file for reading in with pandas
    filename_for_readcsv = _make_file_for_readcsv(filename)
    
    # Open the data file with readcsv
    data_frame = pandas.read_csv(filename_for_readcsv, 
                                 delim_whitespace=True, quoting=3)

    return comments, data_frame


def read_arad(filename):
    """
    Read a shdom adjoint file with "*.adj" file. 
    """
    # Read file
    comments = read_comments(filename)
    
    # Make a special file for reading in with pandas
    filename_for_readcsv = _make_file_for_readcsv(filename)
    
    # Open the data file with readcsv
    data_frame = pandas.read_csv(filename_for_readcsv, 
                                 delim_whitespace=True, quoting=3)

    return comments, data_frame


    


# Script for testing 
if __name__ == "__main__":
    

    # Test file names
    test_files = [
        './shdom_files/les0822nh15t13y135_w0.646_ns1true3.adj',
        './shdom_files/les0822nh15t13y135_w0.646_ns1true3.arad',
        './shdom_files/les0822nh15t13y135_w0.646_ns1true3.log']


    # Use read head
    
