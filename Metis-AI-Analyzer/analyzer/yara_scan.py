import yara

def run_yara(file_path, rule_path="rules/malware_rules.yar"):
    """Run YARA rules against a file and return matches."""
    rules = yara.compile(filepath=rule_path)
    matches = rules.match(file_path)
    return [match.rule for match in matches]
