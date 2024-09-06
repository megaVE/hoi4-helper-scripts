from utils.regex_helper import create_field_regex, create_prefix_regex, check_line_regex
from utils.file_helper import read_file, write_json_file
from utils.list_helper import push_unique_into_list
from utils.debug_helper import debug as debug_helper

NEW_COUNTRY_LEADER_REGEX = create_field_regex('create_country_leader')
HAS_COUNTRY_LEADER_REGEX = create_field_regex('has_country_leader', has_text_content=True)
NAME_REGEX = create_field_regex('name', has_text_content=True)

def main(
  file_path: str = './00_ideologies.txt',
  output_path: str = "ideologies"
) -> None:
  file_lines = read_file(file_path)
  
  # Initial values
  for line in file_lines:
    line = line.strip()
  
  write_json_file(output_path, {})