# banned.py
a Python program to analyze C source code for banned vulnerable functions

## Usage
`python banned.py <input.c> <output.txt>`

## About
There are a number of functions in C code that are known to be vulnerable to possible exploitation. This program helps find these functions to speed up code review. It will print out the line number, what function, and the affected line of code to stdout. It will also create an output file that includes the 2 lines of code before and after each affected line for some context.  
The list of vulnerable functions comes from [git banned.h](https://github.com/git/git/blob/master/banned.h) and [microsoft banned.h](https://github.com/x509cert/banned/tree/master).

### Example
```
$ python banned.py vuln.c output.txt
12: strcpy -> strcpy(dest, "Hello");
13: strcat -> strcat(dest, " World");
15: strncpy -> strncpy(dest, src, 10);
16: strncat -> strncat(dest, src, 5);
18: strcpyA -> strcpyA(dest, src);
19: strcatA -> strcatA(dest, src);
21: _mbscpy -> _mbscpy(dest, src);
22: _mbccpy -> _mbccpy(dest, src);
25: memcpy -> memcpy(dest, src, 50);
26: CopyMemory -> CopyMemory(dest, src, 50);
27: RtlCopyMemory -> RtlCopyMemory(dest, src, 50);
30: IsBadWritePtr -> IsBadWritePtr(dest, 50);
31: IsBadReadPtr -> IsBadReadPtr(src, 50);
34: strtok -> token = strtok(dest, " ");
41: gets -> gets(dest);
42: scanf -> scanf("%s", dest);
45: sprintf -> sprintf(dest, "Number: %d", 42);
46: wsprintf -> wsprintf(dest, L"Wide Number: %d", 42);
50: _splitpath -> _splitpath("C:\\path\\to\\file.txt", drive, dir, fname, ext);
53: alloca -> char *buffer = (char *)alloca(100);
Results written to output.txt
```

#### License
[![GNU General Public License](https://www.gnu.org/graphics/gplv3-88x31.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)\
[![Open Source](http://www.ipol.im/static/badges/open-source.png)](http://www.gnu.org/licenses/gpl.html)\
[![Hacker Emblem](http://catb.org/hacker-emblem/hacker.png)](http://www.catb.org/hacker-emblem/)
