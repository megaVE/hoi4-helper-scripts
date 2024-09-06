def debug(should_debug: bool, debug_message: str) -> None:
  if not should_debug:
    return

  print(debug_message)
