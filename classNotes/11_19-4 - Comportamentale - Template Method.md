# Comportamentale - Template Method

- È un Design Pattern comportamentale che permette di definire i passi di un algoritmo lasciando alle sottoclassi il compito di definire alcuni di questi passi.
- Vediamo un esempio con una classe AbstractWordCounder class che fornisce due metodi:
    - Il primo metodo can_count(filename) restituisce un booleano che indica se la classe può contare le parole del file dato in base all’estensione del file.
    - Il secondo metodo, count(filename) restituisce il conteggio di parole.
- Il codice comprende 2 sottoclassi, una che conta le parole in file di testo e l’altro per contare le parole in file HTML.
- Tutti i metodi sono statici e non si ha a che fare con le istanze della classe.

```python
"""
- il metodo count_words itera su due oggetti classe (sottoclassi della classe astratta)
- se una delle due classi può contare le parole nel file passato a count_words allora viene effettuato il conteggio e
  viene restituito dalla funzione.
- se nessuna delle due classi è in grado di contare le parole, restituisce implicitamente None, non è in grado di contare
"""
def count_words(filename):
	for wordCounter in (PlainTextWordCounter, HtmlWordCounter):
		if wordCounter.can_count(filename):
			return wordCounter.count(filename)
```

- Questa classe (AbstractWordCounter) fornisce i metodi che devono essere implementati nelle eventuali sottoclassi (PlainTextWordCounter) (HtmlWordCounter)
<table>
<tr>
<th> Metodo 1 </th>
<th> Metodo 2 </th>
</tr>
<tr>
<td>

```python
class AbstractWordCounter:

	@staticmethod
	def can_count(filename):
		raise NotImplementedError()

	@staticmethod
	def count(filename):
		raise NotImplementedError()
```

</td>
<td>

```python
class AbstractWordCounter(metaclass=abc.ABCMeta):

	@staticmethod
	@abc.abstractmethod
	def can_count(filename):
		pass

	@staticmethod
	@abc.abstractmethod
	def count(filename):
		pass
```

</td>
</tr>
</table>


```python
import re

class PlainTextWordCounter(AbstractWordCounter):
    @staticmethod
    def can_count(filename):
        """
        Verifica se il file è un file di testo semplice basato sull'estensione.
        """
        return filename.lower().endswith(".txt")

    @staticmethod
    def count(filename):
        """
        Conta le parole in un file di testo semplice.
        """
        if not PlainTextWordCounter.can_count(filename):
            return 0

        regex = re.compile(r"\w+")
        total = 0

        with open(filename, encoding="utf-8") as file:
            for line in file:
                total += len(regex.findall(line))

        return total
```
- re.compile(r"\w+") restituisce un oggetto espressione regolare per fare match di parole
- regex.finditer(line) scandisce line da sinistra a destra e restituisce i match (le parole) nell'ordine in cui li trova