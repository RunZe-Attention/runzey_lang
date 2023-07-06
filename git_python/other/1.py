import dis


def fun(a,b,*args,**kwargs):
    pass

code=fun.__code__

print(code.co_argcount)
print(code.co_posonlyargcount)
print(code.co_kwonlyargcount)




