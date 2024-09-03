from utils.regex_helper import create_field_regex, create_prefix_regex, check_line_regex
from utils.file_helper import read_file, write_json_file
from utils.list_helper import push_unique_into_list

NEW_COUNTRY_LEADER_REGEX = create_field_regex('create_country_leader')
BECOMES_COUNTRY_LEADER_REGEX = create_prefix_regex('_becomes_country_leader')
NAME_REGEX = create_field_regex('name', has_text_content=True)
