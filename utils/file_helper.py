import json, os, codecs

def read_file(file_path: str) -> list[str]:
  """Reads the content from a file and returns an array with each of its lines"""
  if not os.path.isfile(file_path):
    raise Exception(f"The file or path to {file_path} does not exist.")
    
  with codecs.open(file_path, 'r', encoding="utf-8", errors="ignore") as reading_file:
    return reading_file.readlines() 


def write_json_file(file_path: str, file_content: list[any] | dict, indent: int = 4) -> None:
  """Writes a JSON file from an Object or Array"""
  if not os.path.isdir(file_path):
    raise Exception(f"The path to {file_path} is not a valid directory.")
  
  if not ".json" in file_path:
    if len(file_path.split(".").pop()) in [3, 4]:
      file_path = file_path.split(".")
      file_path.pop()
      file_path = ".".join(file_path)
    file_path += ".json"
    
  with open(file_path, 'w') as writting_file:
    writting_file.write(json.dumps(file_content, indent=indent))

  
def show_folder_files(path: str = "./") -> list[str]:
  """Gets a list with all files from a folder"""
  return os.listdir(path)
