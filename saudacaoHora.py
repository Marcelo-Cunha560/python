horario = input('digite um horario (0-23): ')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
       print("Horario deve estar entre 0 e 23.")
    else:
       if horario <= 11:
           print('bom dia!')
       elif horario <= 17:
           print('boa tarde')
       else:
           print('boa noite')
else:
    print('Por favor, digite um horário entre 0 e 23.')
