import subprocess
import re

def main():
    malicious_command_injection_input = "; cd secret_files; cat super_secret_file_1.txt"
    malicious_path_traversal_input = "../secret_files/super_secret_file_2.txt"

    print_header("COMMAND INJECTION EXPLOITATION")
    echo_wrapper_vulnerable("Hello, world!")
    echo_wrapper_vulnerable(malicious_command_injection_input)

    print_header("COMMAND INJECTION MITIGATION")
    echo_wrapper_secure("Hello, world!")
    echo_wrapper_secure(malicious_command_injection_input)

    print_header("PATH TRAVERSAL EXPLOITATION")
    file_reader_vulnerable("boring_public_file.txt")
    file_reader_vulnerable(malicious_path_traversal_input)

    print_header("PATH TRAVERSAL MITIGATION")
    file_reader_secure("boring_public_file.txt")
    file_reader_secure(malicious_path_traversal_input)

def echo_wrapper_vulnerable(text):
    subprocess.run("echo " + text, shell=True)

def echo_wrapper_secure(text):
    # TODO validate the input
    illegal_operators = re.search("[;|&]", text)
    if illegal_operators != None:
        # Illegal operation detected --> exit the wrapper
        print ("\nIllegal Operation Detected: Exiting ...")
        return

    subprocess.run("echo " + text, shell=True)

def file_reader_vulnerable(filepath):
    with open("public_files/" + filepath) as file:
        file_contents = file.read()
        print(file_contents)

def file_reader_secure(filepath):
    # TODO validate the input
    illegal_operators = re.search(".{2}/", filepath)
    if illegal_operators != None:
        # Illegal operation detected --> Exit wrapper
        print ("Illegal Operation Detected: Exiting ...")
        return

    with open("public_files/" + filepath) as file:
        file_contents = file.read()
        print(file_contents)

def print_header(header):
    print(f"\n{'*' * 12} {header}:")

main()
