# Creazionale - Factory Method

- Si usa quando vogliamo definire un’interfaccia o una classe astratta per creare degli oggetti e delegare le sue sottoclassi a decidere quale classe istanziare quando viene richiesto un oggetto.
    - Utile quando una classe non può conoscere in anticipo la classe degli oggetti che deve creare.
- Esempio:
- Consideriamo un framework per delle applicazioni ciascuna delle quali elabora documenti di diverso tipo.
    - Abbiamo bisogno di 2 astrazioni: la classe Application e la classe Document.
        - Application gestisce i documenti e li crea su richiesta dell’utente.
    - Entrambe le classi sono astratte e occorre definire delle loro sottoclassi per poter realizzare le implementazioni relative a ciascuna applicazione.
        - Ad esempio, per creare un’applicazione per disegnare, definiamo le classi DrawingApplication e DrawingDocument.
    - Definiamo un’interfaccia per creare un oggetto ma lasciamo alle sottoclassi decidere quali classi istanziare.
    - Poiché la particolare sottoclasse di Document da istanziare dipende dalla particolare applicazione, la classe Application non può fare previsioni riguardo alla sottoclasse di Document da istanziare.
    - La classe Application sa solo quando deve essere creato un nuovo documento ma non ne conosce il tipo.
    - **Problema**: devono essere istanziare delle classi ma si conoscono solo le classi astratte che non possono essere istanziate!
    - Il factory method pattern risolve questo problema incapsulando l’informazione riguardo alla sottoclasse di Document da creare e sposta questa informazione all’esterno del framework.
    
    ![Untitled](Untitled%209.png)
    
- Le sottoclassi di Application ridefiniscono il metodo astratto CreateDocument per restituire la sottoclasse appropriata di Document.
- Una volta istanziata, la sottoclasse di Application può creare istanze di Document per specifiche applicazioni senza dover conoscere le sottoclassi delle istanze create (CreateDocument).
- CreateDocument è detto factory method perché è responsabile della creazione degli oggetti.

### Esempio

Voglio creare una scacchiera per la dama ed una per gli scacchi

```python
def main():
	checkers = CheckersBoard()
	print(checkers)

	chess = ChessBoard()
	print(chess)
```

```python
BLACK, WHITE = ("BLACK", "WHITE")

class AbstractBoard:

	def __init__(self, rows, columns):
	    self.board = [[None for _ in range(columns)] for _ in range(rows)]
	    self.populate_board()
	
	def populate_board(self):
	    raise NotImplementedError()
	
	def __str__(self):
	    squares = []
	    for y, row in enumerate(self.board):
	        for x, piece in enumerate(row):
	            square = console(piece, BLACK if (y + x) % 2 else WHITE)
	            squares.append(square)
	        squares.append("\\n")
	    return "".join(squares)

```

```python
class CheckersBoard(AbstractBoard):
    def __init__(self):
        super().__init__(10, 10)

    def populate_board(self):
        for x in range(0, 9, 2):
            for row in range(4):
                column = x + ((row + 1) % 2)
                self.board[row][column] = BlackDraught()
                self.board[row + 6][column] = WhiteDraught()

```

```python
class ChessBoard(AbstractBoard):
	def __init__(self):
		super().__init__(8,8)

	def populate_board(self):
		self.board[0][0] = BlackChessRook()
		self.board[0][1] = BlackChessKnight()
		....
		self.board[7][7] = WhiteChessRook()

		for column in range(8):
			self.board[1][column] = BlackChessPawn()
			self.board[6][column] = WhiteChessPawn()
```

```python
class Piece(str):
		__slots__ = () # ci assicuriamo che gli oggetti di tipo Piece non abbiano variabili di istanza
```

```python
class BlackDraught(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\\N{black draughts man}")

class WhiteChessKing(Piece):
    __slots__ = ()

    def __new__(Class):
        return super().__new__(Class, "\\N{white chess king}")

```

Metodo alternativo per popolare la scacchiera di CheckersBoard.

è un **factory method** in quanto dipende dalla factory function create_piece()

```python
def populate_board(self):
	for x in range(0, 9, 2):
		for y in range(4):
			column = x + ((y+1) % 2)
			for row, color in ((y, "black"), (y+6, "white")):
				self.board[row][column] = create_piece("draught", color)
```

```python
def create_piece(kind, color):
	if kind == "draught":
		return eval("{}{}()".format(color.title(), kind.title()))
	return eval("{}Chess{}()".format(color.title(), kind.title()))
```