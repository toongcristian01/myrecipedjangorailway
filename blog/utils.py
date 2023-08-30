import uuid

def get_random_code():
  #limit to 8 chars
  code = str(uuid.uuid4())[:8].replace('-', '').lower()
  return code