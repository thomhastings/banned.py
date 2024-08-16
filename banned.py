import re
import argparse

# List of banned functions as seen in banned.h file
banned_functions = [
    "_mbscpy", "_mbccpy", "strcatA", "strcatW", "_mbscat", "StrCatBuff", "StrCatBuffA", "StrCatBuffW", 
    "StrCatChainW", "_tccat", "_mbccat", "strncpy", "wcsncpy", "_tcsncpy", "_mbsncpy", "_mbsnbcpy", 
    "StrCpyN", "StrCpyNA", "StrCpyNW", "StrNCpy", "strcpynA", "StrNCpyA", "StrNCpyW", "lstrcpyn", 
    "lstrcpynA", "lstrcpynW", "strncat", "wcsncat", "_tcsncat", "_mbsncat", "_mbsnbcat", "lstrncat", 
    "lstrcatnA", "lstrcatnW", "lstrcatn", "IsBadWritePtr", "IsBadHugeWritePtr", "IsBadReadPtr", 
    "IsBadHugeReadPtr", "IsBadCodePtr", "IsBadStringPtr", "memcpy", "RtlCopyMemory", "CopyMemory", 
    "wmemcpy", "lstrlen", "strcpy", "strcpyA", "strcpyW", "wcscpy", "_tcscpy", "_mbscpy", "StrCpy", 
    "StrCpyA", "StrCpyW", "lstrcpy", "lstrcpyA", "lstrcpyW", "_tccpy", "_mbccpy", "_ftcscpy", 
    "strcat", "strcatA", "strcatW", "wcscat", "_tcscat", "_mbscat", "StrCat", "StrCatA", "StrCatW", 
    "lstrcat", "lstrcatA", "lstrcatW", "StrCatBuff", "StrCatBuffA", "StrCatBuffW", "StrCatChainW", 
    "_tccat", "_mbccat", "_ftcscat", "sprintfW", "sprintfA", "wsprintf", "wsprintfW", "wsprintfA", 
    "sprintf", "swprintf", "_stprintf", "wvsprintf", "wvsprintfA", "wvsprintfW", "vsprintf", 
    "_vstprintf", "vswprintf", "strncpy", "wcsncpy", "_tcsncpy", "_mbsncpy", "_mbsnbcpy", "StrCpyN", 
    "StrCpyNA", "StrCpyNW", "StrNCpy", "strcpynA", "StrNCpyA", "StrNCpyW", "lstrcpyn", "lstrcpynA", 
    "lstrcpynW", "strncat", "wcsncat", "_tcsncat", "_mbsncat", "_mbsnbcat", "StrCatN", "StrCatNA", 
    "StrCatNW", "StrNCat", "StrNCatA", "StrNCatW", "lstrncat", "lstrcatnA", "lstrcatnW", "lstrcatn", 
    "gets", "_getts", "_gettws", "IsBadWritePtr", "IsBadHugeWritePtr", "IsBadReadPtr", 
    "IsBadHugeReadPtr", "IsBadCodePtr", "IsBadStringPtr", "memcpy", "RtlCopyMemory", "CopyMemory", 
    "wmemcpy", "lstrlen", "wnsprintf", "wnsprintfA", "wnsprintfW", "vsnprintf", "wvnsprintf", 
    "wvnsprintfA", "wvnsprintfW", "strtok", "_tcstok", "wcstok", "_mbstok", "makepath", "_tmakepath", 
    "_makepath", "_wmakepath", "_splitpath", "_tsplitpath", "_wsplitpath", "scanf", "wscanf", 
    "_tscanf", "sscanf", "swscanf", "_stscanf", "snscanf", "snwscanf", "_sntscanf", "_itoa", "_itow", 
    "_i64toa", "_i64tow", "_ui64toa", "_ui64tot", "_ui64tow", "_ultoa", "_ultot", "_ultow", "CharToOem", 
    "CharToOemA", "CharToOemW", "OemToChar", "OemToCharA", "OemToCharW", "CharToOemBuffA", 
    "CharToOemBuffW", "alloca", "_alloca", "ChangeWindowMessageFilter", "wnsprintf", "wnsprintfA", 
    "wnsprintfW", "_snwprintf", "_snprintf", "_sntprintf", "_vsnprintf", "vsnprintf", "_vsnwprintf", 
    "_vsntprintf", "wvnsprintf", "wvnsprintfA", "wvnsprintfW", "strtok", "_tcstok", "wcstok", 
    "_mbstok", "makepath", "_tmakepath", "_makepath", "_wmakepath", "_splitpath", "_tsplitpath", 
    "_wsplitpath", "scanf", "wscanf", "_tscanf", "sscanf", "swscanf", "_stscanf", "snscanf", 
    "snwscanf", "_sntscanf", "_itoa", "_itow", "_i64toa", "_i64tow", "_ui64toa", "_ui64tot", "_ui64tow", 
    "_ultoa", "_ultot", "_ultow", "CharToOem", "CharToOemA", "CharToOemW", "OemToChar", "OemToCharA", 
    "OemToCharW", "CharToOemBuffA", "CharToOemBuffW", "alloca", "_alloca", "ChangeWindowMessageFilter"
]

# Function to search for banned functions and create detailed output
def search_banned_functions(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    results = []

    for i, line in enumerate(lines, start=1):
        for function in banned_functions:
            # Regular expression to find the function calls in the code
            pattern = rf'\b{function}\b\s*\('
            if re.search(pattern, line):
                # Capture context: two lines before and after
                start_context = max(0, i - 3)  # Two lines before
                end_context = min(len(lines), i + 2)  # Two lines after
                context = lines[start_context:end_context]
                print(f"{i}: {function} -> {line.strip()}")
                results.append((i, function, line.strip(), context))

    # Write results to the output file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        if results:
            for line_num, func_name, line_text, context in results:
                out_file.write(f"Function '{func_name}' found at line {line_num}:\n")
                out_file.write(f"Affected line: {line_text}\n")
                out_file.write("Context (2 lines before and after):\n")
                for context_line in context:
                    out_file.write(context_line)
                out_file.write("\n\n" + "-"*50 + "\n\n")
            print(f"Results written to {output_file}")
        else:
            out_file.write("No banned functions found in the source code.\n")
            print("No banned functions found in the source code.")

# Main function to handle command-line arguments and execute the search
def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Search C source code for banned functions.")
    parser.add_argument('input_file', help="Path to the C source code file")
    parser.add_argument('output_file', help="Path to the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Call the search function with the provided arguments
    search_banned_functions(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
