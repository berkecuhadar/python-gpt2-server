from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")  
def generate(user_input: str):
    query = f"Query: {user_input} [END]"
    input_ids = tokenizer.encode(query, return_tensors="pt",truncation=True)
    output = model.generate(input_ids, max_length=50+len(user_input), num_return_sequences=1, temperature=0.7, pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id, do_sample=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    response = response.replace(query, "").strip()
    response = response.replace("Answer: ", "").strip()
    return response
