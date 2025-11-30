# 🛡️ File Type Identification Tool (Magic Numbers)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A defensive security tool that detects potential malware disguised with fake file extensions. It analyzes binary file headers ("magic numbers") to identify the true file type and flags mismatches.

## 🧐 The Problem

Malware often hides in plain sight by using fake file extensions. An executable file (`.exe`) might be renamed to `invoice.pdf` or `vacation.jpg` to trick users into clicking it. Operating systems often rely on these extensions to decide which application to open, but the underlying binary content reveals the truth.

## 💡 The Solution

This tool ignores the file extension and looks at the **Magic Numbers**—the unique byte signatures at the beginning of a file that define its format.

**Example:**
- A file named `image.jpg` should start with `FF D8 FF`.
- If it starts with `4D 5A` (the signature for an Executable), this tool will flag it immediately.

## 🚀 Features

- **Binary Analysis**: Reads raw hex signatures from file headers.
- **Mismatch Detection**: Automatically compares detected type vs. file extension.
- **Recursive Scanning**: Scans entire directories for hidden threats.
- **Container Awareness**: Distinguishes between simple mismatches and container formats (e.g., ZIPs used for DOCX).

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/file-type-id.git
    cd file-type-id
    ```

2.  **Install dependencies** (optional, for colored output):
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

Run the tool against a file or a directory:

```bash
python main.py <path_to_file_or_directory>
```

### Example Output

```text
Scanning 5 files...

STATUS                    | DETECTED   | EXTENSION  | FILE
--------------------------------------------------------------------------------
Match                     | jpg        | jpg        | test_files\valid.jpg
MISMATCH                  | exe        | jpg        | test_files\malware_disguised.jpg  <-- DETECTED!
MISMATCH                  | pdf        | txt        | test_files\secret.txt             <-- DETECTED!
Unknown Type              | ???        | txt        | test_files\random.txt
--------------------------------------------------------------------------------

[!] Found 2 mismatches! Potential disguised files.
```

## 🧠 Skills Demonstrated

- **Binary File Analysis**: Handling file I/O in binary mode and parsing hex signatures.
- **Defensive Programming**: Building tools to validate data integrity and detect anomalies.
- **Python Development**: Creating structured, modular CLI applications.
- **System Administration**: Automating file system scanning and verification.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
