import re, sys
from utils.file_helper import read_file, write_json_file
from utils.regex_helper import  create_prefix_regex, create_field_regex
from utils.wrapper_score_helper import calculate_wrapper_score, Bracket

# Commandline Params
should_debug = False
if len(sys.argv) > 1:
  should_debug = sys.argv[1]
  if re.match(should_debug, r'should_debug\s*=\sTrue.*'):
    should_debug = True
    print("Debug mode is ON.")

# ./common/ideologies/
FILE_PATH = './00_ideologies.txt'
IDEOLOGIES = ["democratic", "fascism", "communism", "neutrality"]
IDEOLOGY_NAME_REGEX = create_prefix_regex("\\s*=\\s*{")
SUBIDEOLOGY_REGEX = create_field_regex("types")
SUBIDEOLOGY_NAME_REGEX = create_prefix_regex("\\s*=\\s*{")

# Aux functions
def create_empty_ideology_dictionary() -> dict["name": str, "types": list[str]]:
  return {
    "name": None,
    "types": []
  }


def get_match_from_list(match_list: list):
  for match in match_list:
    if match:
      return match
  
  return None


def debug(string):
  if should_debug:
    print(string)


file_lines = read_file(FILE_PATH)

bracket_score = -1
ideology_data = create_empty_ideology_dictionary()
ideology_list = {}
is_inside_subideology_list = False
for line in file_lines:
  line = line.strip()
  bracket_score += calculate_wrapper_score(line, Bracket.CURLY_BRACKETS)
  
  # Ideology Sublist Checking
  if ideology_data["name"]:
    if is_inside_subideology_list:
      # Checks if subideology list ended
      if bracket_score == 1:
        is_inside_subideology_list = False
    else:
      # Checks if subideology list started
      if re.match(SUBIDEOLOGY_REGEX, line):
        is_inside_subideology_list = True
  
  if bracket_score == 1 and not ideology_data["name"]:
    # Checks for ideologies groups
    ideologies_match = re.match(IDEOLOGY_NAME_REGEX, line)
    if ideologies_match: # and ideologies_match.group(1) in IDEOLOGIES:
      ideology_data["name"] = ideologies_match.group(1).strip()
  
  if bracket_score == 0 and ideology_data["name"]:
    # Pushes ready ideology object into list
    ideology_list[ideology_data["name"]] = ideology_data["types"]
    ideology_data = create_empty_ideology_dictionary()
  
  if is_inside_subideology_list:
    # Checks for subideologies
    subideology_match = re.match(SUBIDEOLOGY_NAME_REGEX, line)
    if subideology_match:
      ideology_data["types"] += [subideology_match.group(1).strip()]

if ideology_list:
  write_json_file("ideology_list", ideology_list)
else:
  print("No ideologies available for file.")