from transformers import AutoModelForCausalLM, AutoTokenizer

def cargar_modelo():
    modelo = AutoModelForCausalLM.from_pretrained("DeepESP/gpt2-spanish")
    tokenizer = AutoTokenizer.from_pretrained("DeepESP/gpt2-spanish")
    return modelo, tokenizer