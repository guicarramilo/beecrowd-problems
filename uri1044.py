def multiplos():
    A, B= map(float, input().split())
    if B % A == 0 or A % B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

multiplos()
multiplos()