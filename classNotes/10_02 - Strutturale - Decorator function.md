# Strutturale - Decorator

- Serve quando vogliamo estendere le funzionalità di singoli oggetti dinamicamente.
- Ad esempio un sistema GUI dovrebbe consentire di aggiungere proprietà (come i bordi) o comportamenti (lo scrolling) ad ogni componente dell’interfaccia utente.
- Un modo per far questo è tramite l’ereditarietà. Ereditare un bordo da un’altra classe mette un bordo intorno ad ogni istanza della sottoclasse.
    - Ciò è poco flessibile perché la scelta di un bordo è fatta in modo statico. Non è possibile controllare come e quando decorare la componente con un bordo.
- Un altro approccio più flessibile consiste nel racchiudere la componente in un altro oggetto che si occupa di aggiungere il bordo.
- Questo oggetto è definito “decoratore”.
- Il decoratore inoltra richieste alla componente e può svolgere azioni aggiuntive, come aggiungere un bordo o altre proprietà.

### Il Pattern Decorator (è una funzione)

- Un decoratore **__di funzione__** è una funzione che ha come unico argomento una **funzione** e restituisce una funzione con lo stesso nome della funzione originale ma con ulteriori funzionalità.
- Un decoratore **__di classe__** è una funzione che ha come unico argomento una **classe** e restituisce una classe con lo stesso nome della classe originale ma con funzionalità aggiuntive.
    - I decoratori di classe possono a volte essere utilizzati come alternativa alla creazione di sottoclassi.
- In Python c’è un supporto built-in per i decoratori di funzioni e per i decoratori di classe

### Function Decorator

- Tutti i decoratori di funzione hanno la stessa struttura:
    - Creazione della funzione wrapper:
        - all’interno del wrapper invochiamo la funzione originale;
        - prima di invocare la funzione originale possiamo effettuare qualsiasi lavoro di pre-processing;
        - dopo la chiamata siamo liberi di acquisire il risultato, di fare qualsiasi lavoro di post-processing e di restituire qualsiasi valore vogliamo;
    - Alla fine restituiamo la funzione wrapper come risultato del decoratore e questa funzione sostituisce la funzione originale acquisendo il suo nome.
    - Si scrive il simbolo @, allo stesso livello di indentazione dello statement def, seguito immediatamente dal nome del decoratore.
        - è possibile applicare un decoratore ad una funzione decorata.
    
    ```python
    #la nostra funzione decoratore
    def float_args_and_return(function):
        def wrapper(*args, **kwargs):
            args = [float(arg) for arg in args]
            return float(function(*args, **kwargs))
        return wrapper
    
    @float_args_and_return
    def mean(first, second, *rest):
        numbers = (first, second) + rest
        return sum(numbers) / len(numbers)
    
    ```
    
    Con la versione decorata, mean(5, “6”, “7.5”) non genera alcun errore dal momento che viene effettuato il casting in numeri validi.
    
    È anche possibile creare una funzione senza decoratore ed aggiungerlo successivamente così:
    
    ```python
    def mean(first, second, *rest):
        numbers = (first, second) + rest
        return sum(numbers) / len(numbers)
    
    mean = float_args_and_return(mean)
    
    ```
    

### Analizziamo bene il codice di sopra

- La funzione *float_args_and_return()* è un decoratore di funzione per cui ha come argomento una singola funzione.
- Per convenzione, le funzioni wrapper hanno come argomenti un parametro che indica il numero variabile di parametri (*args) ed uno di tipo keyword (***kwargs)
- Eventuali vincoli sugli argomenti sono gestiti dalla funzione originale. Nel creare il decoratore, **dobbiamo solo assicurarci che alla funzione originale vengano passati tutti gli argomenti.**

### Problema di Documentazione del codice

- Una funzione decoratore avrà il valore dell’attributo **\_\_name__** settato a **wrapper** invece che con il nome originale della funzione.
- Non ha docstring anche nel caso in cui la funzione originale abbia una docstring!
- Attraverso un ulteriore decoratore **@functools.wraps** per decorare la funzione wrapper possiamo assicurarci che gli attributi \_\_name__ e \_\_doc__ della funzione decorata contengano rispettivamente il nome e la docstring della funzione originale.
- È sempre consigliato usare il decoratore @functools.wrap dal momento che ci assicura che:
    - nei traceback vengano visualizzati i nomi corretti delle funzioni
    - E si possa accedere alle docstring delle funzioni originali

```python
import functools

def float_args_and_return(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args = [float(arg) for arg in args]
        return float(function(*args, **kwargs))
    return wrapper

```

Esercizio

- Scrivere il decoratore di funzione decf che fa in modo che venga lanciata l’eccezione TypeError se il numero di argomenti è diverso da due. Altrimenti, se la funzione decorata restituisce un risultato, questo viene aggiunto insieme al valore del primo argomento in un file di nome “risultato.txt”.
- Suggerimento: Ricordatevi di convertire a stringa il valore del primo argomento e il risultato quando li scrivete nel file e di aprire il file in modo da non cancellare quanto scritto precedentemente nel file.

```python
def decf(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if(len(args)+len(kwargs)=!2):
			raise TypeError("function must have 2 arguments!")
		else
			result = function(*args, **kwargs)
			#qui continuiamo a scrivere la funzione decoratore
			with open("risultato.txt", "a") as file:
				arg1 = str(args[0])
				result_str = str(result)
	
				file.write(arg1 + " + " result_str + " = " + str(float(arg1) + float(result_str)) + "\n")
			#abbiamo finito la funzione decoratore
		return result
	return wrapper

#ora utilizziamolo seriamente:

def somma(a, b)
	return a + b

try:
	somma(2, 3)
except TypeError as e:
	print(e)
```

- Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia l’eccezione TypeError se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa formata dagli argomenti ricevuti in input e dal risultato intervallati da uno spazio. Non dimenticate di convertire il risultato in stringa quando lo inserite nella stringa output.
- Esempio: se la funzione riceve in input “il” , “risultato”, “è”, la funzione non lancia l’eccezione e restituisce la stringa “Il risultato è …” dove al posto dei puntini deve apparire il risultato della funzione.