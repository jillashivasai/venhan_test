def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")
