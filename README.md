# Scripts and CSV scores for calculation of music persistent homology
This repository includes scripts and csv scores to create distance matrices.

## Make a score csv file
Insert key signature names in the first column. I prepared some examples.

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
