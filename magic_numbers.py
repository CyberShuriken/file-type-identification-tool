# Dictionary mapping hex signatures (as bytes) to file extensions
# We use a list of tuples or a dictionary where keys are bytes.
# Some formats have offsets, but for this simple tool we'll focus on starting bytes.

MAGIC_NUMBERS = {
    b'\xFF\xD8\xFF': 'jpg',
    b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'png',
    b'\x47\x49\x46\x38\x37\x61': 'gif',
    b'\x47\x49\x46\x38\x39\x61': 'gif',
    b'\x25\x50\x44\x46': 'pdf',
    b'\x50\x4B\x03\x04': 'zip', # Also used for docx, xlsx, jar, etc. usually
    b'\x50\x4B\x05\x06': 'zip', # Empty zip
    b'\x50\x4B\x07\x08': 'zip', # Spanned zip
    b'\x4D\x5A': 'exe', # DOS MZ executable (dll, exe)
    b'\x7F\x45\x4C\x46': 'elf',
    b'\x52\x61\x72\x21\x1A\x07\x00': 'rar',
    b'\x52\x61\x72\x21\x1A\x07\x01\x00': 'rar',
    b'\x1F\x8B': 'gz',
    b'\x49\x44\x33': 'mp3',
    b'\xFF\xFB': 'mp3',
    b'\x00\x00\x01\xBA': 'mpg',
    b'\x00\x00\x01\xB3': 'mpg',
    b'\x66\x74\x79\x70\x69\x73\x6F\x6D': 'mp4', # ftypisom
    b'\x42\x4D': 'bmp',
}

# Mapping of "umbrella" types to extensions if needed, or just simple normalization
# For example, 'jpeg' and 'jpg' are the same.
EXTENSION_MAP = {
    'jpeg': 'jpg',
    'htm': 'html',
}

def get_max_header_length():
    return max(len(sig) for sig in MAGIC_NUMBERS.keys())
