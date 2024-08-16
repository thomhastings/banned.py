#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>

void test_banned_functions() {
    char src[50], dest[50];
    char *token;
    FILE *file;
    
    // Unsafe string copy functions
    strcpy(dest, "Hello");
    strcat(dest, " World");

    strncpy(dest, src, 10);
    strncat(dest, src, 5);

    strcpyA(dest, src);
    strcatA(dest, src);
    
    _mbscpy(dest, src);
    _mbccpy(dest, src);
    
    // Unsafe memory copy functions
    memcpy(dest, src, 50);
    CopyMemory(dest, src, 50);
    RtlCopyMemory(dest, src, 50);

    // Dangerous pointer operations
    IsBadWritePtr(dest, 50);
    IsBadReadPtr(src, 50);

    // Unsafe token parsing
    token = strtok(dest, " ");
    
    // Dangerous file operations
    file = tmpfile();
    fclose(file);

    // Unsafe I/O functions
    gets(dest);
    scanf("%s", dest);
    
    // Unsafe formatting functions
    sprintf(dest, "Number: %d", 42);
    wsprintf(dest, L"Wide Number: %d", 42);

    // Unsafe path manipulation
    char drive[_MAX_DRIVE], dir[_MAX_DIR], fname[_MAX_FNAME], ext[_MAX_EXT];
    _splitpath("C:\\path\\to\\file.txt", drive, dir, fname, ext);

    // Unsafe memory allocation
    char *buffer = (char *)alloca(100);
    
    // Potentially risky system function
    system("dir");
}

int main() {
    test_banned_functions();
    return 0;
}