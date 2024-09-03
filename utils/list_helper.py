def push_unique_into_list(object_list: list[dict], new_object: dict, id_field: str = "name") -> None:
  """Inserts a dictionary into a list if it is unique"""
  for existing_object in object_list:
    if existing_object.get(id_field) == new_object.get(id_field):
      return
  
  object_list.append(new_object)
