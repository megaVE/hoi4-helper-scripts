from re import match, Pattern

def create_field_regex(field_name: str, has_text_content: bool = False) -> Pattern[str]:
  """Checks and/or extracts the content after a certain regex"""
  post_equal_content = '"*([\\w\\s]+)"*' if has_text_content else '{'
  return fr'.*{field_name}\s*=\s*{post_equal_content}'


def create_prefix_regex(post_text: str) -> Pattern[str]:
  """Checks and/or extracts the content before a certain regex"""
  return fr'([\w\s]+){post_text}.*'


def check_line_regex(line: str, object_data: dict, attribute_name: str, attribute_regex: Pattern[str], ok_value: any = True, has_text_content: bool = False) -> None:
  """Checks if a string matches a regex and updates a dictionary according to it"""
  if attribute_name in object_data and object_data[attribute_name]:
    return
  
  attribute_match = match(attribute_regex, line)
  if attribute_match:
    object_data[attribute_name] = attribute_match.group(1) if has_text_content else ok_value
