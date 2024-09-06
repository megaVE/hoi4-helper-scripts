import re, sys

from utils.regex_helper import check_line_regex, create_field_regex
from utils.wrapper_score_helper import calculate_bracket_score, Bracket
from utils.file_helper import read_file, write_json_file
from utils.list_helper import push_unique_into_list
from utils.debug_helper import debug as debug_helper

# Commandline Params
should_debug = False
if len(sys.argv) > 1:
  should_debug = sys.argv[1]
  if re.match(should_debug, r'should_debug\s*=\sTrue.*'):
    should_debug = True
    print("Debug mode is ON.")

# Regexes
NAME_REGEX = create_field_regex('name', has_text_content=True)
IS_LEADER_REGEX = create_field_regex('country_leader')
IS_ARMY_GENERAL_REGEX = create_field_regex('corps_commander')
IS_ARMY_FIELD_MARSHAL = create_field_regex('field_marshal')
IS_ADMIRAL_REGEX = create_field_regex('navy_leader')
ADVISOR_ROLE_REGEX = create_field_regex('slot', has_text_content=True)

# Aux Functions
def create_empty_character_dictionary():
  return {
    'is_country_leader': False,
    'army_role': None,
    'is_navy_leader': False,
    'advisor_role': None
  }

def debug(string: str) -> None:
  debug_helper(should_debug, string)


def main(file_path: str, output_path: str) -> None:
  file_lines = read_file(file_path)
  
  bracket_score = -1
  current_character_data = create_empty_character_dictionary()
  character_list = []
  for line in file_lines:
    line = line.strip()
    debug(line)
    bracket_score += calculate_bracket_score(line, Bracket.CURLY_BRACKETS)
    
    if bracket_score == 0 and 'name' in current_character_data:
      push_unique_into_list(character_list, current_character_data)
      current_character_data = create_empty_character_dictionary()

    # Name
    check_line_regex(line, current_character_data, 'name', NAME_REGEX)
    # Leader
    check_line_regex(line, current_character_data, 'is_country_leader', IS_LEADER_REGEX, ok_value=True)
    # Army
    check_line_regex(line, current_character_data, 'army_role', IS_ARMY_GENERAL_REGEX, ok_value="general")
    check_line_regex(line, current_character_data, 'army_role', IS_ARMY_FIELD_MARSHAL, ok_value="field_marshal")
    # Navy
    check_line_regex(line, current_character_data, 'is_navy_leader', IS_ADMIRAL_REGEX, ok_value=True)
    # Advisor
    check_line_regex(line, current_character_data, 'advisor_role', ADVISOR_ROLE_REGEX)
    
    debug(current_character_data)

  if len(character_list) == 0:
    print(f'No characters available for "{file_path}".')
  else:
    write_json_file(output_path, character_list)
