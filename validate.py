import re

def validate_name(name):
    return re.search(r"(-?([A-Z].\s)?([A-Z][a-z]+)\s?)+([A-Z]'([A-Z][a-z]+))?", name)