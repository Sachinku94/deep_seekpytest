import pytest
from deepseek_client.deepseek_api import DeepSeekClient
from utils.executor import execute_generated_code

@pytest.mark.functional
def test_run_deepseek_generated_task():
    client = DeepSeekClient()
    
    task_prompt = """
    Write a Python Selenium script that:
    - Opens https://uatev.jioinsure.in/
    - Closes popup if present
    - Selects 'Health' option
    - Fills random mobile number
    - Fills random PIN code
    - Clicks on Get Free Quote
    - Ends session
    """
    
    code = client.generate_code(task_prompt)
    
    with open("generated_code/temp_script.py", "w") as f:
        f.write(code)
    
    success = execute_generated_code()
    assert success, "Generated script failed to execute properly."
