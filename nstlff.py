import os
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

if __name__ == "__main__":
    for root, dirs, files in os.walk("./test/"):
        for folder in dirs:
            abs_path = os.path.join(root, folder)
            if not checkEntry(folder, abs_path, True):
                print(f"Folder '{folder}' in '{root}' does not match the specified pattern.")
        for file in files:
            abs_path = os.path.join(root, file)
            if not checkEntry(file, abs_path, False):
                print(f"File '{file}' in '{root}' does not match the specified pattern.")
