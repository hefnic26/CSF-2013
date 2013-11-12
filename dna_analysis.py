# Name: Nicholas Hefling
# Evergreen Login: hefnic26
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
g_count = 0
a_count = 0
c_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

    if bp == 'A' or bp == 'T':
        # increment the count of gc
        at_count = at_count + 1

    # if nucleotide is G
    if bp == 'G':
    # increment the count of g
        g_count = g_count + 1

    # if nucleotide is a
    elif bp == 'A':
    # increment the count of a
        a_count = a_count + 1

    # if nucleotide is C
    elif bp == 'C':
    # increment the count of a
        c_count = c_count + 1

    #if nucleotide is T
    elif bp == 'T':
    # increment the count of a
        t_count = t_count + 1

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count

# divide the G, A, T, C counts by respective total counts
g_content = float(g_count) / total_count
a_content = float(a_count) / total_count
t_content = float(t_count) / total_count
c_content = float(c_count) / total_count

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'A Count:', a_count
print 'T Count:', t_count
print 'G Count:', g_count
print 'C Count:', c_count
print 'Sum Count:', sum_count
print 'Total Count:', total_count
print 'Length of sequence:', len(seq)
print 'AT/GC Ratio:', AT_GC_Ratio

if gc_content > 0.6:
    print 'CG Classification: This is a high GC content organism'
elif gc_content < 0.4:
    print 'CG Classification: This is a low GC content organism'
else:
    print 'CG Classification: This is a moderate GC content organism'
