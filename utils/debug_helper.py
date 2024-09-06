import sys, re

def check_if_should_debug() -> bool:
  if len(sys.argv) > 1:
    should_debug = sys.argv[1]
    if re.match(should_debug, r'should_debug\s*=\sTrue.*'):
      print("Debug mode is ON.")
      return True

  return False

def debug(
  debug_message: str,
  should_debug: bool = check_if_should_debug()
) -> None:
  if not should_debug:
    return

  print(debug_message)
