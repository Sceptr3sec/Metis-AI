import hashlib
import magic

def get_hashes(file_path):
    """Return MD5 and SHA256 hashes of a file."""
    hashes = {}
    with open(file_path, "rb") as f:
        data = f.read()
        hashes["md5"] = hashlib.md5(data).hexdigest()
        hashes["sha256"] = hashlib.sha256(data).hexdigest()
    return hashes

def get_file_type(file_path):
    """Identify file type using magic signatures."""
    return magic.from_file(file_path)

def extract_strings(file_path, min_length=4):
    """Extract readable strings from a file."""
    results = []
    with open(file_path, "rb") as f:
        data = f.read()
        current = []
        for byte in data:
            if 32 <= byte <= 126:  # printable ASCII
                current.append(chr(byte))
            else:
                if len(current) >= min_length:
                    results.append("".join(current))
                current = []
        if len(current) >= min_length:
            results.append("".join(current))
    return results