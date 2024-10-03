import os, json


def main(script_name: str = "file_lister.py", output_name: str = "output.json"):
  """Lists all files from a folder in a JSON array format"""
  file_list = list(filter(lambda x: x not in [script_name, output_name], os.listdir()))

  with open(f"./{output_name}", 'w') as writting_file:
    writting_file.write(json.dumps(file_list, indent=4))