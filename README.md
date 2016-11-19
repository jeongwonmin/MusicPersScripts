# A script for calculation of music persistent homology
This is a script to create distance matrix csv of a "score" (as a csv file).

## Make a score csv
Input key signature names. Left is our input.

- 'c'= C
- 'cs' = C#
- 'd' = D
- 'ds' = D#
- 'e' = E
- 'f' = F
- 'fs' = F#
- 'g' = G
- 'gs' = G#
- 'a' = A
- 'as' = A#
- 'b' = B

## Create a distance matrix csv
python3 distance_matrix.py --dim n path/to/inputcsv path/to/outputcsv

- --dim is 1, 2 or 3.
- This python code is only for python3. 
