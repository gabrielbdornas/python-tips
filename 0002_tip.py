# Minha maneira inicial
squares = []
for i in range(10):
  squares.append(i*i)
print(f'Primeiro: {squares}')

# Maneira mais fácil
new_squares = [i*i for i in range(10)]
print(f'Segundo: {new_squares}')
print(f'Segundo == Primeiro: {new_squares == squares}')

