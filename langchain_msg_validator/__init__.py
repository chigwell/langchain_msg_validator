# __init__.py

import re

def is_valid_langchain_message(message: str) -> bool:
    """
    Validates if a given string is a plausible Langchain message.

    This function performs basic structural checks, looking for common patterns
    found in AI-generated messages, particularly those structured by frameworks
    like Langchain. It does not perform deep semantic analysis or verify
    external data sources.

    Args:
        message: A multiline string representing the AI message.

    Returns:
        True if the message appears to be a valid Langchain message, False otherwise.
    """
    if not isinstance(message, str) or not message.strip():
        return False

    # Check for common starting patterns (e.g., "Here's", "The", "Sure,")
    # or direct answers without introductory phrases.
    starts_plausibly = re.match(r"^(Here's|The|Sure,|Okay,|Certainly,)\s", message, re.IGNORECASE) or \
                       re.match(r"^\s*[A-Za-z]", message) # Starts with a word

    # Check for common ending patterns (e.g., punctuation, polite closings)
    ends_plausibly = re.search(r"[.!?]$|\.$|\.$|\n$", message.strip()) or \
                     re.search(r"(?i)(?:thank you|best regards|sincerely)$", message.strip())

    # Presence of some form of content (more than just whitespace or very short)
    has_content = len(message.strip()) > 10

    # Basic check for internal structure - presence of multiple sentences or distinct thoughts
    # This is a very heuristic check.
    sentence_count = len(re.split(r'[.!?]+', message.strip()))
    has_structure = sentence_count >= 1 and len(message.splitlines()) > 1 or sentence_count > 1

    return starts_plausibly and ends_plausibly and has_content and has_structure
