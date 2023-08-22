def write_file(file_name, file_content):
    try:
        with open(file_name + ".txt", "w") as file:
            file.write(file_content)
    except FileNotFoundError:
        return "File not found"

def append_to_file(file_name, append_content):
    try:
        with open(file_name + ".txt", "a") as file:
            file.write(append_content)
    except FileNotFoundError:
        return "File not found"

def read_file(file_name):
    try:
        with open(file_name + ".txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found"
