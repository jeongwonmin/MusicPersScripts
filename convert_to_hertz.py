import argparse
import numpy as np
import csv

# Frequencies for each note
C = 261.63
C_SHARP = 277.18
D = 293.66
D_SHARP	= 311.13
E = 329.63
F = 349.23
F_SHARP = 369.99
G = 392
G_SHARP = 415.3
A =	440
A_SHARP = 466.16
B = 493.88

def alph_to_freq(alph):
    if alph == 'c':
        return C
    if alph == 'cs':
        return C_SHARP
    if alph == 'd':
        return D
    if alph == 'ds':
        return D_SHARP
    if alph == 'e':
        return E
    if alph == 'f':
        return F
    if alph == 'fs':
        return F_SHARP
    if alph == 'g':
        return G
    if alph == 'gs':
        return G_SHARP
    if alph == 'a':
        return A
    if alph == 'as':
        return A_SHARP
    if alph == 'b':
        return B



if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description='write frequency sequence csv file')
    parser.add_argument('--dim', metavar='d', type=int, help='create d-tuple')
    parser.add_argument('infile', nargs='?', metavar='infile', default='/Users/MIN/Music/folklore/pers_of_folklore/test.csv', help='input file path')
    parser.add_argument('outfile', nargs='?', metavar='outfile', default='/Users/MIN/Music/folklore/pers_of_folklore/out.csv', help='output file path')
    args = parser.parse_args()


    if args.dim == 1:
        
        freq_array = []
        
        with open(args.infile, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                freq_array.append(alph_to_freq(row[0]))

        with open(args.outfile, 'w') as writef:
            writer = csv.writer(writef, lineterminator='\n')
            writer.writerow(freq_array)

    if args.dim == 2:
        
        freq_array = []
        freq_row = []
    
        with open(args.infile, 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                freq_row.append(alph_to_freq(row[0]))

        freq_array.append(freq_row[:len(freq_row)-1])
        freq_array.append(freq_row[1:])

        with open(args.outfile, 'w', newline='') as writef:
            writer = csv.writer(writef, dialect='excel', delimiter=",", lineterminator="\n")
            writer.writerows(freq_array)

    if args.dim == 3:

        freq_array = []
        freq_row = []
        
        with open(args.infile, 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                freq_row.append(alph_to_freq(row[0]))
    
        freq_array.append(freq_row[:len(freq_row)-2])
        freq_array.append(freq_row[1:len(freq_row)-1])
        freq_array.append(freq_row[2:len(freq_row)])
        
        with open(args.outfile, 'w', newline='') as writef:
            writer = csv.writer(writef, dialect='excel', delimiter=",", lineterminator="\n")
            writer.writerows(freq_array)
