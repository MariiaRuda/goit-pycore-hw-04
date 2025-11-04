import os
import sys
from color import color_directory, color_file

def visualize_directory_structure(path):
    path = os.path.abspath(path)
    
    if not os.path.exists(path):
        print(f"🚫 Path '{path}' does not exist.")
        return
    if not os.path.isdir(path):
        print(f"⚠️  Path '{path}' is not a directory.")
        return
    
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{color_directory(os.path.basename(root))}/")
        
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{color_file(f)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚙️  Usage: python visualize_structure.py <path_to_directory>")
    else:
        visualize_directory_structure(sys.argv[1])
