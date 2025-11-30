import argparse
import sys
import os
from detector import check_file_mismatch
try:
    from colorama import init, Fore, Style
    init()
    RESET = Style.RESET_ALL
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
except ImportError:
    # Fallback if colorama is not installed
    RESET = ""
    RED = ""
    GREEN = ""
    YELLOW = ""

def main():
    parser = argparse.ArgumentParser(description="File Type Identification Tool - Detect Magic Number Mismatches")
    parser.add_argument("path", help="Path to the file or directory to analyze")
    
    args = parser.parse_args()
    target_path = args.path
    
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        sys.exit(1)

    files_to_scan = []
    
    if os.path.isfile(target_path):
        files_to_scan.append(target_path)
    else:
        for root, dirs, files in os.walk(target_path):
            for file in files:
                files_to_scan.append(os.path.join(root, file))
                
    print(f"Scanning {len(files_to_scan)} files...\n")
    print(f"{'STATUS':<25} | {'DETECTED':<10} | {'EXTENSION':<10} | {'FILE'}")
    print("-" * 80)
    
    mismatch_count = 0
    
    for filepath in files_to_scan:
        result = check_file_mismatch(filepath)
        
        status = result['status']
        detected = result['detected_type'] if result['detected_type'] else "???"
        ext = result['original_extension']
        
        color = RESET
        if result['mismatch']:
            color = RED
            mismatch_count += 1
        elif status == 'Match' or status == 'Match (Container Format)':
            color = GREEN
        else:
            color = YELLOW
            
        print(f"{color}{status:<25} | {detected:<10} | {ext:<10} | {filepath}{RESET}")

    print("-" * 80)
    if mismatch_count > 0:
        print(f"\n{RED}[!] Found {mismatch_count} mismatches! Potential disguised files.{RESET}")
    else:
        print(f"\n{GREEN}[+] Scan complete. No obvious mismatches found.{RESET}")

if __name__ == "__main__":
    main()
