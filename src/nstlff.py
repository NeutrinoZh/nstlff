import os
import rule

def main():
    for root, dirs, files in os.walk("./test/"):

            for folder in dirs:
                abs_path = os.path.join(root, folder)
                if not rule.checkEntry(folder, abs_path, True):
                    print(f"Folder '{folder}' in '{root}' does not match the specified pattern.")

            for file in files:
                abs_path = os.path.join(root, file)
                if not rule.checkEntry(file, abs_path, False):
                    print(f"File '{file}' in '{root}' does not match the specified pattern.")


if __name__ == "__main__":
    main()    