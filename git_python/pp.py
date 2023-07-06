'''
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2", torchscript=True).eval()

# tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
in_text = "Lionel Messi is a"
tmp = tokenizer.encode(in_text)

print(tokenizer.decode(torch.tensor([43])))
print(tokenizer.decode(torch.tensor([295])))
print(tokenizer.decode(torch.tensor([417])))
print(tokenizer.decode(torch.tensor([36128])))
print(tokenizer.decode(torch.tensor([318])))
print(tokenizer.decode(torch.tensor([257])))
print(tokenizer.decode(torch.tensor([2137])))
print(len(tokenizer))

print("198这是啥啊")
print(tokenizer.decode(torch.tensor([198])))
in_tokens = torch.tensor(tmp)


# inference
token_eos = torch.tensor([198])  # line break symbol
out_token = None
i = 0
with torch.no_grad():
    while out_token != token_eos:
        print(f'step {i} 序列长度: {len(in_tokens)}', flush=True)
        logits, _ = model(in_tokens)
        out_token = torch.argmax(logits[-1, :], dim=0, keepdim=True)
        in_tokens = torch.cat((in_tokens, out_token), 0)
        text = tokenizer.decode(in_tokens)
        print(f'step {i} input: {text}', flush=True)
        i += 1

out_text = tokenizer.decode(in_tokens)
print(f' Input: {in_text}')
print(f'Output: {out_text}')
'''


import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


model = GPT2LMHeadModel.from_pretrained("gpt2", torchscript=True).eval()

# tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
in_text = "Lionel Messi is a"
in_tokens = torch.tensor(tokenizer.encode(in_text))

# inference
token_eos = torch.tensor([198]) # line break symbol
out_token = None
kvcache = None
out_text = in_text
i = 0
with torch.no_grad():
    while out_token != token_eos:
        logits, kvcache = model(in_tokens, past_key_values=kvcache) # 增加了一个 past_key_values 的参数
        out_token = torch.argmax(logits[-1, :], dim=0, keepdim=True)
        in_tokens = out_token # 输出 token 直接作为下一轮的输入，不再拼接
        text = tokenizer.decode(in_tokens)
        print(f'step {i} input: {text}', flush=True)
        i += 1
        out_text += text

print(f' Input: {in_text}')
print(f'Output: {out_text}')
