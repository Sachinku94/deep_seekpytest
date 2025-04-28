from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class DeepSeekClient:
    def __init__(self, model_path="deepseek-v3-model"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def generate_code(self, task_prompt):
        inputs = self.tokenizer(task_prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=300)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
