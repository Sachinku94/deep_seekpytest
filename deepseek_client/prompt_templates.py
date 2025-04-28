# Example template for task descriptions
BROWSER_TASK_TEMPLATE = """
Write a Python Selenium script that:
- Opens {url}
- Closes any pop-up if present
- Selects '{dropdown_option}' from the dropdown with id '{dropdown_id}'
- Fills a random mobile number in the field with id '{mobile_field_id}'
- Fills a random PIN code in the field with id '{pincode_field_id}'
- Clicks the button with id '{button_id}'
- Ends session gracefully after execution.
"""
