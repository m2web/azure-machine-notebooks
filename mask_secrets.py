#!/usr/bin/env python3
import re
import os
import argparse
import json

def mask_text(content):
    """
    Scans text content for common secret patterns and masks their values.
    """
    # Patterns for keys, tokens, secrets, passwords, and endpoints
    patterns = [
        r'(?i)(key|secret|token|password|endpoint|subscription_id)\s*[:=]\s*(["\'])(?:(?!\2).)*\2',
    ]
    
    masked_content = content
    for pattern in patterns:
        def replace_match(match):
            key_name = match.group(1)
            quotes = match.group(2)
            return f'{key_name} = {quotes}********{quotes}'
            
        masked_content = re.sub(pattern, replace_match, masked_content)
    
    return masked_content

def process_ipynb(file_path, inplace=False):
    """
    Special handling for Jupyter Notebooks (JSON format).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            nb_data = json.load(f)
        
        changed = False
        for cell in nb_data.get('cells', []):
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                new_source = []
                for line in source:
                    masked_line = mask_text(line)
                    if masked_line != line:
                        changed = True
                    new_source.append(masked_line)
                cell['source'] = new_source
        
        if changed:
            if inplace:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(nb_data, f, indent=1)
                print(f"Masked and saved (IPYNB): {file_path}")
            else:
                print(f"--- Masked output for {file_path} (IPYNB) ---")
                print(json.dumps(nb_data, indent=1))
                print("-" * 40)
        else:
            print(f"No secrets found in: {file_path}")
            
    except Exception as e:
        print(f"Error processing IPYNB {file_path}: {e}")

def process_file(file_path, inplace=False):
    if file_path.endswith('.ipynb'):
        process_ipynb(file_path, inplace)
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        masked = mask_text(content)
        
        if masked != content:
            if inplace:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(masked)
                print(f"Masked and saved: {file_path}")
            else:
                print(f"--- Masked output for {file_path} ---")
                print(masked)
                print("-" * 40)
        else:
            print(f"No secrets found in: {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scan and mask secrets in code files.")
    parser.add_argument("path", help="Path to a file or directory to scan.")
    parser.add_argument("--inplace", action="store_true", help="Modify files in place.")
    parser.add_argument("--ext", default=".py,.ipynb,.md", help="Comma-separated list of extensions to scan (default: .py,.ipynb,.md).")
    
    args = parser.parse_args()
    extensions = tuple(args.ext.split(','))
    
    if os.path.isfile(args.path):
        process_file(args.path, args.inplace)
    elif os.path.isdir(args.path):
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file.endswith(extensions):
                    process_file(os.path.join(root, file), args.inplace)
    else:
        print(f"Path not found: {args.path}")

if __name__ == "__main__":
    main()
