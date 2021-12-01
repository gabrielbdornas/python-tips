# Minha maneira inicial
data = [1,2,-3,-4]
print(f'Primeiro: {data}')
for i in range(len(data)):
  if data[i] < 0:
    data[i] = 0
print(f'Primeiro: {data}')

# Maneira mais fácil
new_data = [1,2,-3,-4]
for idx, num in enumerate(new_data):
  if num < 0:
    data[idx] = 0
print(f'Segundo: {data}')
