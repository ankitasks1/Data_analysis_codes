import os,sys
#import matplotlib.pyplot as plt
#import numpy as np

def reads_explorer(myfasta):
    read = 1
    readdist = []
    readlength = []
    for lines in myfasta:
        if not lines.startswith(">"):
            myout = ''.join(str(read) + '\t' + str(len(lines)))
            readdist.append(myout)
            readlength.append((len(lines)))
            read += 1
    return readlength

def base_replace(myfasta):
    lines1 = []
    for lines in myfasta:
        if not lines.startswith(">"):
            #print(type(lines))
            lines.replace("a", "T")
            lines.replace("t", "A")
            lines.replace("g", "C")
            lines.replace("c", "G")
            lines1.append(lines)
    return lines1

def base_composition(adjfasta):
    A = 0
    T = 0
    G = 0
    C = 0
    N = 0
    for sequence in adjfasta:
        sequence = list(sequence)
        for base1 in sequence:
            #print(base1)
            if "A" in base1:
                A += 1
            elif "T" in base1:
                T += 1
            elif "G" in base1:
                G += 1
            elif "C" in base1:
                C += 1
            elif "N" in base1:
                N += 1
    print(''.join("Composition of A is " + str(round(float(float(A * 100) / float((A + T + G + C))), 2)) + "%"))
    print(''.join("Composition of T is " + str(round(float(float(T * 100) / float((A + T + G + C))), 2)) + "%"))
    print(''.join("Composition of G is " + str(round(float(float(G * 100) / float((A + T + G + C))), 2)) + "%"))
    print(''.join("Composition of C is " + str(round(float(float(C * 100) / float((A + T + G + C))), 2)) + "%"))
    print(''.join("Composition of N is " + str(round(float(float(N * 100) / float((A + T + G + C))), 2)) + "%"))

myfasta = open(sys.argv[1], "r")
myfasta =myfasta.read().strip().split("\n")
adjfasta = base_replace(myfasta)
base_composition(adjfasta)

#Calculate Min, Max read length and Total Bases
readseq = reads_explorer(myfasta)
print("Total Bases in Fasta file are: " + str(sum(readseq)))
print("Minimum read length is: " + str(min(readseq)))
print("Maximum read length is: " + str(max(readseq)))

#Calculate Mean read length
number_of_reads = len(readseq)
print("Mean read length is: " + str((sum(readseq))//(number_of_reads)))

#Calculate Median read length
readseq.sort()
if number_of_reads % 2 == 0:
    median1 = readseq[number_of_reads // 2]
    median2 = readseq[number_of_reads // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = readseq[number_of_reads // 2]
print("Median read length is: " + str(median))


# Initialize layout
#fig, ax = plt.subplots(figsize = (9, 9))

#plot
#ax.hist(readseq, bins=10, edgecolor="black")