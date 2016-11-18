import argparse
import numpy as np
import csv
import math

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

#distance between a and b
def distance1(a, b):
    return min(abs(math.log2(a)-math.log2(b)), 1 - abs(math.log2(a)-math.log2(b)))

#distance between (a1, a2) and (b1, b2)
def distance2(a1, a2, b1, b2):
    return min(distance1(a1,b1)+distance1(a2,b2),
               distance1(a1,b2)+distance1(a2,b1))

def distance3(a1, a2, a3, b1, b2, b3):
    dist123 = distance1(a1,b1) + distance1(a2,b2) + distance1(a3,b3)
    
    dist132 = distance1(a1,b1) + distance1(a2,b3) + distance1(a3,b2)

    dist213 = distance1(a1,b2) + distance1(a2,b1) + distance1(a3,b3)
    
    dist231 = distance1(a1,b2) + distance1(a2,b3) + distance1(a3,b1)
    
    dist312 = distance1(a1,b3) + distance1(a2,b1) + distance1(a3,b2)
    
    dist321 = distance1(a1,b3) + distance1(a2,b2) + distance1(a3,b1)
    
    return min(dist123, dist132, dist213, dist231, dist312, dist321)

if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description='write frequency sequence csv file')
    parser.add_argument('--dim', metavar='d', type=int, help='create d-tuple')
    parser.add_argument('infile', nargs='?', metavar='infile', default='./test.csv', help='input file path')
    parser.add_argument('outfile', nargs='?', metavar='outfile', default='./out_dist.csv', help='output file path')
    args = parser.parse_args()


    if args.dim == 1:
        
        freq_array = []

        with open(args.infile, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                freq_array.append(alph_to_freq(row[0]))
    
        distance_matrix = []
        distance_row = []
    
        for j in range(0, len(freq_array)):
            for i in range(0, len(freq_array)):
                distance_row.append(distance1(freq_array[j], freq_array[i]))
            distance_matrix.append(distance_row[len(freq_array)*j:len(freq_array)*(j+1)])

        with open(args.outfile, 'w') as writef:
            writer = csv.writer(writef, lineterminator='\n')
            writer.writerows(distance_matrix)

    if args.dim == 2:
        
        freq_array = []
        freq_row = []
        distance_matrix = []
    
        with open(args.infile, 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                freq_row.append(alph_to_freq(row[0]))

        freq_array.append(freq_row[:len(freq_row)-1])
        freq_array.append(freq_row[1:])

        distance_matrix = []
        distance_row = []
        
        for j in range(0, len(freq_array[0])):
            for i in range(0, len(freq_array[0])):
                distance_row.append(distance2(freq_array[0][j], freq_array[1][j],
                                              freq_array[0][i], freq_array[1][i]))
            distance_matrix.append(distance_row[len(freq_array[0])*j:len(freq_array[0])*(j+1)])
        
        with open(args.outfile, 'w') as writef:
            writer = csv.writer(writef, lineterminator='\n')
            writer.writerows(distance_matrix)


    if args.dim == 3:

        freq_array = []
        freq_row = []
        distance_matrix = []
        
        with open(args.infile, 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                freq_row.append(alph_to_freq(row[0]))
    
        freq_array.append(freq_row[:len(freq_row)-2])
        freq_array.append(freq_row[1:len(freq_row)-1])
        freq_array.append(freq_row[2:len(freq_row)])
        
        distance_matrix = []
        distance_row = []

        for j in range(0, len(freq_array[0])):
            for i in range(0, len(freq_array[0])):
                distance_row.append(distance3(freq_array[0][j], freq_array[1][j], freq_array[2][j],
                                      freq_array[0][i], freq_array[1][i], freq_array[2][i]))
            distance_matrix.append(distance_row[len(freq_array[0])*j:len(freq_array[0])*(j+1)])
                
        with open(args.outfile, 'w') as writef:
            writer = csv.writer(writef, lineterminator='\n')
            writer.writerows(distance_matrix)


    #for test
    print(distance_matrix)
    print(freq_array)
    print(C)
    print(C_SHARP)
    print(D)
