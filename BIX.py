print('BIX: Dati che riguardano il militare')
print('Non distribuire i nostri dati nei circuiti di controinformazione!')

passw = input('Inserire la password: ')

pagamento = str(input("Vuole pagare? (Scriva Yes o No): "))
pagamento.lower()

if pagamento != 'yes':
    print('Arrivederci!')
    
modalita = str(input('Modalità di pagamento \n(1 per Carta di credito, 2 per Contocorrente della ditta, 3 per Contocorrente personale) \nCome vuole pagare?  '))    
    
if modalita != '1':
    print('Arrivederci!')
    
tipoCC = str(input('Digiti il tipo di carta di credito (Visa, Matercard, ...): '))
tipoCC.lower()

if tipoCC != 'visa':
    print('Arrivederci!')
    
nomeBanca = str(input('Inserisca il nome della Banca: '))

numCC = str(input('Inserisca il numero di carta di credito: '))

#print(numCC)
corretto = str(input('Il numero è corretto? (Yes o No): '))

print('Il numero di carta di credito è autorizzato')

print("E' autorizzato ad entrare e ad utilizzare i nostri servizi")
database = str(input("Digiti 'Yes' se vuole accedere al servizio di database: "))

soggetto = str(input("Per cosa vuole cercare l'argomento? "))

armi = str(input('Cosa vuole cercare? '))

print('Attenzione questa area contiene informazioni riservate.')
codiceAccessoSpeciale = str(input("Introdurre il codice di accesso speciale: "))

print('La vostra richiesta è stata accettata')

print('#1 - 1301 Tactical \n#2 - A400 \n#3 - 1301 Comp \n#4 - 98 A1 \n#5 - 694 \n#6 - 695 \n#7 - DT11 \n#8 - SL3')

selezioneItem = str(input('Digiti il numero di item selezionato: '))

