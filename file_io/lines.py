import sys
import os

from sys_arg_len import sys_arg_len

sys_arg_len(2)

path = sys.argv[1]

if ".py" not in path:
    sys.exit("Not a Python file")

count = 0

script_dir = os.path.dirname(__file__)
try:
    # Accessing file in a relative direct
    with open(os.path.join(script_dir, path)) as file:
        for line in file:
            stripped_line = line.strip()

            if stripped_line and not "#" in stripped_line:
                count += 1
                
except FileNotFoundError:
    sys.exit("File is not found")

print(count)

"""
    import sys
    import os

    def main():
        if len(sys.argv) != 2:
            sys.exit("Usage: python script.py <filename.py>")
        
        path = sys.argv[1]

        if not path.endswith(".py"):
            sys.exit("Not a Python file")

        count = 0
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, path)
        
        try:
            with open(file_path) as file:
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line and not stripped_line.startswith("#"):
                        count += 1
        except FileNotFoundError:
            sys.exit("File not found")

        print(count)

    if __name__ == "__main__":
        main()

"""