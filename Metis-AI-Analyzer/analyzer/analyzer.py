from analyzer import static, yara_scan

def analyze_file(file_path):
    results = {}

    # Hashes
    results["hashes"] = static.get_hashes(file_path)

    # File type
    results["file_type"] = static.get_file_type(file_path)

    # Strings (count only to avoid huge outputs)
    strings = static.extract_strings(file_path)
    results["string_count"] = len(strings)

    # YARA matches
    results["yara_matches"] = yara_scan.run_yara(file_path)

    return results
