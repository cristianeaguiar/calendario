# importar biblioteca
import calendar

# gera calendário do mês desejado
ano = int(input("Informe o ano desejado: "))
mes = int(input("Informe o número do mês desejado:"))

if mes > 0 and mes <=12:
    print(calendar.month(ano,mes))
else:
    print("Mês inválido")