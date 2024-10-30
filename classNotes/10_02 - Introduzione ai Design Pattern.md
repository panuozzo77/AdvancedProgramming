La **Gang of Four** (GOF) ha introdotto il concetto di Design Pattern. Hanno osservato che ciò che Christopher Alexander esprime riguardo ai pattern negli edifici e nelle città è vero anche quando si parla di object-oriented design pattern. 

# Cos’è un Design Pattern

- Forniscono schemi generali per la soluzione di problematiche ricorrenti che si incontrano durante lo sviluppo software.
- Favoriscono il riutilizzo di tecniche di design di successo nello sviluppo di nuove soluzioni.
- Evitano al progettista di riscoprire ogni volta le stesse cose.
- Permettono di sviluppare un linguaggio comune che semplifica la comunicazione tra le persone coinvolte nello sviluppo del software.

## Caratterizzazione

- **Nome del Pattern**. Associare un nome consente un elevato livello di astrazione e facilita la comunicazione tra gli addetti.
- **Il Problema**. Descrive in quali contesti ha senso applicare il pattern.
- **La Soluzione**. Fornisce la descrizione astratta di un problema e indica come utilizzare gli strumenti a disposizione per risolverlo.
- **Le Conseguenze**. Descrivono i risultati dell’applicazione del design pattern. Esse sono fondamentali per valutare le diverse alternative e comprendere i costi e benefici risultanti dall’applicazione del pattern.

### Elenco dei Design Pattern

1. Adapter
• 2.Facade
• 3.Composite
• 4.Decorator
• 5.Bridge
• 6.Singleton
• 7.Proxy
• 8.Flyweight
• 9.Strategy
• 10.State
• 11.Command
• 12.Observer

Memento
14.Interpreter
15.Iterator

Visitor
17.Mediator
18.Template Method
19.Chain of Responsibility
20.Builder
21.Prototype
22.Factory Method
23.Abstrac Factory

## Classificazione

- I Pattern **Creazionali** riguardano il processo di creazione degli oggetti
- I Pattern **Strutturali** riguardano la composizione di classi ed oggetti
- I Pattern **Comportamentali** caratterizzano il modo in cui le classi e gli oggetti interagiscono tra di loro e si distribuiscono le responsabilità.

**Design Pattern Creazionali**

- Astraggono il processo di creazione
- Aiutano a rendere il sistema indipendente da come i suoi oggetti sono creati, composti e rappresentati.
- Diventano utili man mano che il sistema diventa sempre più indipendente dalla composizione di oggetti. Man mano che ciò accade, l’enfasi si sposta dalla codifica di un insieme fissato di comportamenti alla definizione di un insieme più piccolo di comportamenti fondamentali che possono essere composti per dar vita a comportamenti più complessi.

**Design Pattern Strutturali**

- Riguardano le relazioni tra entità quali classi e oggetti.
- Forniscono metodologie semplici per comporre oggetti per creare nuove funzionalità.

**Design Pattern Comportamentali**

- Riguardano il modo in cui le cose vengono fatte, in altre parole, gli algoritmi e le interazioni tra gli oggetti.
- Forniscono modi efficaci per pensare e organizzare la computazione.
- Alcuni di questi pattern sono built-in in Python.