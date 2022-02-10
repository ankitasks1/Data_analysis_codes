import os,sys

ref_subNnat_R1_rc = open(input('Enter fasta file: '), 'r')
ref_subNnat_R1_rc = ref_subNnat_R1_rc.read()
ref_subNnat_R1_rc = ref_subNnat_R1_rc.strip().split('\n')
#print(ref_subNnat_R1_rc)

header = ref_subNnat_R1_rc[0]
header = header.split(' ')
#print(header)
coordinates = header[1]


start  = coordinates.strip().split(':')
start  = start[1].strip().split('-')

sequence = ref_subNnat_R1_rc[1]
#print(sequence)
sequence = list(sequence)
SeqStart = 0
count = 0
for i in range(0,len(sequence)):
    SeqStart += 1
    #print(SeqStart)
    twobase = sequence[SeqStart: SeqStart + 2]
    twobase = ''.join(twobase)
    #print(twobase)

    if twobase == 'CG':
        count += 1
        CGsites = "".join(twobase + str(count))
        CGStart = "".join(str(int(SeqStart) + int(start[0])))
        CGsiteStart = "".join(CGsites + '\t' + CGStart)
        print(CGsiteStart)
        with open('CGSites.txt', 'a') as myfile:
            myfile.write(CGsiteStart +'\n')
            myfile.close()
    else:
        pass


