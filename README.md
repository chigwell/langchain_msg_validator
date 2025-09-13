[![PyPI version](https://badge.fury.io/py/langchain-msg-validator.svg)](https://badge.fury.io/py/langchain-msg-validator)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/langchain-msg-validator)](https://pepy.tech/project/langchain-msg-validator)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# langchain_msg_validator

`langchain_msg_validator` is a Python package that provides a simple utility function to perform basic validation on strings intended to be Langchain messages. It checks for common structural patterns to heuristically determine if a message is likely to be a well-formed AI-generated response.

## Installation

To install `langchain_msg_validator`, use pip:

```bash
pip install langchain-msg-validator
```

## Usage

Using `langchain_msg_validator` is straightforward. Import the `is_valid_langchain_message` function and pass your message string to it.

```python
from langchain_msg_validator import is_valid_langchain_message

message1 = "Here's a summary of the document:\n\nThis document discusses the importance of AI."
message2 = "This is not a valid message."
message3 = ""

print(f"Message 1 is valid: {is_valid_langchain_message(message1)}")
print(f"Message 2 is valid: {is_valid_langchain_message(message2)}")
print(f"Message 3 is valid: {is_valid_langchain_message(message3)}")
```

Expected output:
```
Message 1 is valid: True
Message 2 is valid: False
Message 3 is valid: False
```

## Features

- Basic structural validation for AI-generated messages.
- Checks for plausible starting and ending patterns.
- Ensures the message has sufficient content and basic structure.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/langchain_msg_validator/issues).

## License

`langchain_msg_validator` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Author

Eugene Evstafev <hi@eugene.plus>
Repository: https://github.com/chigwell/langchain_msg_validator