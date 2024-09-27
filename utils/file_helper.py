import json, os, codecs

def read_file(file_path: str) -> list[str]:
  """Reads the content from a file and returns an array with each of its lines"""
  with codecs.open(file_path, 'r', encoding="utf-8", errors="ignore") as reading_file:
    return reading_file.readlines() 


def write_json_file(file_path: str, file_content: list[any] | dict, indent: int = 4) -> None:
  """Writes a JSON file from an Object or Array"""
  if not ".json" in file_path:
    file_path += ".json"
    
  with open(file_path, 'w') as writting_file:
    writting_file.write(json.dumps(file_content, indent=indent))

  
def show_folder_files(path: str = "./") -> list[str]:
  """Gets a list with all files from a folder"""
  return os.listdir(path)
