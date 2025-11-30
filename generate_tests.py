import os

def create_file(filename, content_bytes):
    with open(filename, 'wb') as f:
        f.write(content_bytes)
    print(f"Created {filename}")

def main():
    os.makedirs('test_files', exist_ok=True)
    
    # 1. Valid JPEG
    # JPEG magic number: FF D8 FF
    create_file('test_files/valid.jpg', b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46')
    
    # 2. Valid PNG
    # PNG magic number: 89 50 4E 47 0D 0A 1A 0A
    create_file('test_files/valid.png', b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D')
    
    # 3. Disguised EXE as JPG (Malware scenario)
    # EXE magic number: 4D 5A
    create_file('test_files/malware_disguised.jpg', b'\x4D\x5A\x90\x00\x03\x00\x00\x00')
    
    # 4. Disguised PDF as TXT
    # PDF magic number: 25 50 44 46
    create_file('test_files/secret.txt', b'\x25\x50\x44\x46\x2D\x31\x2E\x35')
    
    # 5. Unknown type (Random text)
    create_file('test_files/random.txt', b'Just some random text content here.')

if __name__ == "__main__":
    main()
