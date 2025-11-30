import os
from magic_numbers import MAGIC_NUMBERS, get_max_header_length, EXTENSION_MAP

def identify_file_type(filepath):
    """
    Reads the file header and returns the detected extension based on magic numbers.
    Returns None if no match is found.
    """
    max_len = get_max_header_length()
    
    try:
        with open(filepath, 'rb') as f:
            header = f.read(max_len)
    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
        return None

    # Check for matches. We check longer signatures first to be more specific if needed,
    # but iterating through the dict is usually fine if keys are distinct enough.
    # A better approach for overlapping signatures is to sort by length descending.
    
    sorted_signatures = sorted(MAGIC_NUMBERS.keys(), key=len, reverse=True)
    
    for sig in sorted_signatures:
        if header.startswith(sig):
            return MAGIC_NUMBERS[sig]
            
    return None

def check_file_mismatch(filepath):
    """
    Checks if the file's extension matches its detected content type.
    Returns a dictionary with results.
    """
    detected_type = identify_file_type(filepath)
    
    _, ext = os.path.splitext(filepath)
    original_ext = ext.lower().lstrip('.')
    
    # Normalize extension if needed
    original_ext = EXTENSION_MAP.get(original_ext, original_ext)
    
    result = {
        'filepath': filepath,
        'original_extension': original_ext,
        'detected_type': detected_type,
        'mismatch': False,
        'status': 'Unknown'
    }
    
    if detected_type:
        if original_ext == detected_type:
            result['status'] = 'Match'
            result['mismatch'] = False
        else:
            # Special case: ZIP magic number is used for many formats (docx, apk, jar)
            # For this simple tool, we might flag them, but let's add a note.
            if detected_type == 'zip' and original_ext in ['docx', 'xlsx', 'pptx', 'jar', 'apk']:
                 result['status'] = 'Match (Container Format)'
                 result['mismatch'] = False
            else:
                result['status'] = 'MISMATCH'
                result['mismatch'] = True
    else:
        result['status'] = 'Unknown Type'
        
    return result
