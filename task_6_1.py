list_result = []
with open('nginx_logs.txt', "r", encoding="utf-8") as f:
    for line in f:
        values = line.split()
        list_result.append((values[0], values[5].strip('"'), values[6]))
print(list_result)
