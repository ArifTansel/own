
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("TURKCELL/Turkcell-LLM-7b-v1")
tokenizer = AutoTokenizer.from_pretrained("TURKCELL/Turkcell-LLM-7b-v1")

messages = [
    {"role": "user", "content": "Türkiye'nin başkenti neresidir?"},
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

eos_token = tokenizer("<|im_end|>",add_special_tokens=False)["input_ids"][0]

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, 
                               max_new_tokens=1024, 
                               do_sample=True, 
                               eos_token_id=eos_token)
                               
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
