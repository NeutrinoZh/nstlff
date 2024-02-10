import re

class Rule:
    def __init__(self, pattern, file_naming: str, folder_naming: str) -> None:
        self.pattern = pattern
        self.file_naming = file_naming
        self.folder_naming = folder_naming

rules = [
    Rule(r".*", r"[a-z]*.test", r"[A-Z][a-zA-Z]*"),
]

def checkEntry(name: str, abs_name: str, is_folder: bool) -> bool:
    def checkName(rule: Rule) -> bool:
        if is_folder:
            return re.fullmatch(rule.folder_naming, name)
        return re.fullmatch(rule.file_naming, name)

    for rule in rules:
        is_match = re.fullmatch(rule.pattern, abs_name)
        if is_match:
            is_match = checkName(rule)
            if not is_match:
                return False
            break
    else:
        return False
    
    return True