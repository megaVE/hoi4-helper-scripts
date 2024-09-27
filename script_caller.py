from utils.file_helper import show_folder_files

import common_characters_reader

scripts = {
  "common_characters_reader": common_characters_reader.main
}

def show_message(text: str) -> None:
  print("-" * len(text))
  print(text)
  print("-" * len(text))

def request_input(input_variable: any) -> None:
  input_variable = input("\n>")

def process_script_index(index: int) -> str:
  counter = 0
  last_script = ""
  for script_key in scripts:
    last_script = script_key
    if counter == index:
      break
  
    counter += 1

  return last_script

show_message("Please enter the script you'd like to choose:")
index = 0
for key in scripts:
  print(f"{index}: {key}")
  index += 1

selected_script = int(input("\n> "))
selected_script = process_script_index(selected_script)
if not selected_script in scripts:
  show_message("Invalid script!")
  quit()
selected_script = scripts[selected_script]

file_path = input("Please enter the file's input path: ")
files = show_folder_files(file_path)
if not files:
  show_message("Invalid source folder.")
  quit()
output_path = input("Please enter the file's input output: ")

for file in files:
  selected_script(file_path=f"{file_path}/{file}", output_path=f"{output_path}/{file}")