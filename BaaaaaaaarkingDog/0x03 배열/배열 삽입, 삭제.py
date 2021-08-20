def insert(idx, value, arar):
    temp = arar[idx:]
    arar[idx] = value
    return arar[:idx+1] + temp
	
def erase(idx, arar):
    temp = arar[idx+1:]
    return arar[:idx]+temp