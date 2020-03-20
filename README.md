# Labor Netztechnik - Spanning Tree
## Usage
Run script with:
```bash
python3 __main__.py -i files/graph.st
```
Files with graph data are stored in the files directory.

Node declaration, maximum one space between characters allowed:
```bash
A = 5;      allowed
A=5;        allowed
   A = 5;   allowed
A  =  5;    not allowed
```
Link declaration, maximum one space between characters allowed:
```bash
A - B: 5;       allowed
A-B:5;          allowed
   A - B: 5;    allowed
A  -  B :   5;  not allowed
```
