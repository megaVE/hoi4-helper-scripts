from enum import Enum

class Bracket(Enum):
  PARENTHESIS = 1
  BRACKETS = 2
  CURLY_BRACKETS = 3
  

def calculate_wrapper_score(string: str, bracket_type: Bracket) -> int:
  """Allows to count the openning and closing brackets from a whole string"""
  if bracket_type == Bracket.PARENTHESIS:
    return string.count('(') - string.count(')')
  
  if bracket_type == Bracket.BRACKETS:
    return string.count('[') - string.count(']')
    
  if bracket_type == Bracket.CURLY_BRACKETS:
    return string.count('{') - string.count('}')
  