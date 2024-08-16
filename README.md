# banned.py
a Python program to analyze C source code for banned vulnerable functions

# Usage
`python banned.py <input.c> <output.txt>`

# Background
There are a number of functions in C code that are known to be vulnerable to possible exploitation. This program helps find these functions to speed up code review. It will print out the line number, what function, and the affected line of code to stdout. It will also create an output file that includes the 2 lines of code before and after the affected line for some context.
The list of vulnerable functions comes from [git banned.h](https://github.com/git/git/blob/master/banned.h) and [microsoft banned.h](https://github.com/x509cert/banned/tree/master).

#### License
[![GNU General Public License](https://www.gnu.org/graphics/gplv3-88x31.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)\
[![Open Source](http://www.ipol.im/static/badges/open-source.png)](http://www.gnu.org/licenses/gpl.html)\
[![Hacker Emblem](http://catb.org/hacker-emblem/hacker.png)](http://www.catb.org/hacker-emblem/)
