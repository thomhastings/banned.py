import re
import argparse

# List of banned functions as seen in banned.h file
banned_functions = [
    "ChangeWindowMessageFilter", "CharToOem", "CharToOemA", "CharToOemBuffA", "CharToOemBuffW", "CharToOemW", 
    "CopyMemory", "IsBadCodePtr", "IsBadHugeReadPtr", "IsBadHugeWritePtr", "IsBadReadPtr", "IsBadStringPtr", 
    "IsBadWritePtr", "OemToChar", "OemToCharA", "OemToCharW", "RtlCopyMemory", "StrCat", "StrCatA", "StrCatBuff", 
    "StrCatBuffA", "StrCatBuffW", "StrCatChainW", "StrCatN", "StrCatNA", "StrCatNW", "StrCatW", "StrCpy", "StrCpyA", 
    "StrCpyN", "StrCpyNA", "StrCpyNW", "StrCpyW", "StrNCat", "StrNCatA", "StrNCatW", "StrNCpy", "StrNCpyA", 
    "StrNCpyW", "_alloca", "_ftcscat", "_ftcscpy", "_getts", "_gettws", "_i64toa", "_i64tow", "_itoa", "_itow", 
    "_makepath", "_mbccat", "_mbccpy", "_mbscat", "_mbscpy", "_mbsnbcat", "_mbsnbcpy", "_mbsncat", "_mbsncpy", 
    "_mbstok", "_snprintf", "_sntprintf", "_sntscanf", "_snwprintf", "_splitpath", "_stprintf", "_stscanf", "_tccat", 
    "_tccpy", "_tcscat", "_tcscpy", "_tcsncat", "_tcsncpy", "_tcstok", "_tmakepath", "_tscanf", "_tsplitpath", 
    "_ui64toa", "_ui64tot", "_ui64tow", "_ultoa", "_ultot", "_ultow", "_vsnprintf", "_vsntprintf", "_vsnwprintf", 
    "_vstprintf", "_wmakepath", "_wsplitpath", "alloca", "asctime", "asctime_r", "ctime", "ctime_r", "gets", "gmtime", 
    "localtime", "lstrcat", "lstrcatA", "lstrcatW", "lstrcatn", "lstrcatnA", "lstrcatnW", "lstrcpy", "lstrcpyA", 
    "lstrcpyW", "lstrcpyn", "lstrcpynA", "lstrcpynW", "lstrlen", "lstrncat", "makepath", "memcpy", "scanf", "snscanf", 
    "snwscanf", "sprintf", "sprintfA", "sprintfW", "sscanf", "strcat", "strcatA", "strcatW", "strcpy", "strcpyA", 
    "strcpyW", "strcpynA", "strncat", "strncpy", "strtok", "strtok_r", "swprintf", "swscanf", "vsnprintf", "vsprintf", 
    "vswprintf", "wcscat", "wcscpy", "wcsncat", "wcsncpy", "wcstok", "wmemcpy", "wnsprintf", "wnsprintfA", 
    "wnsprintfW", "wscanf", "wsprintf", "wsprintfA", "wsprintfW", "wvnsprintf", "wvnsprintfA", "wvnsprintfW", 
    "wvsprintf", "wvsprintfA", "wvsprintfW"
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
