Array di microfoni e beamforming
Ilaria Martella
Melania Moras

	Introduzione agli array di sorgenti o riceventi
Abbiamo visto la configurazione ad array di antenne per la propagazione o ricevimento di onde elettromagnetiche, eviudenziando le caratteristiche e parametri principali di tale configurazione.
In particolare abbiamo visto che il campo totale irradiato da un array di antenne è divisibile in due componenti: la prima che dipende dalla struttura della singola antenna e la seconda, detta array factor, che invece dipende solo dalla geometria dell’array. Abbiamo inoltre effettuato delle valutazioni sul campo totale dell’array, che può essere rappresentato come diagramma di radiazione presentante dei massimi (interferenza costruttiva) e dei minimi (interferenza distruttiva). Tale distribuzione è fondamentale per le tecnologie che si basano proprio su queste zone di interferenza costruttiva e distruttiva per indirizzare il segnale proprio verso i target desiderati, invece di propagare le onde elettromagnetiche in tutte le direzioni indistintamente. Tali tecnologie prendono il nome di beamforming, ove “beam” indica il fascio irradiato dall’array.

	Beamforming nelle applicazioni audio
Anche in ambito acustico la configurazione ad array reca i vantaggi del beamforming, sia per dispositivi trasmissivi (altoparlanti) sia per dispositivi riceventi (microfoni).
In particolare, focalizzandoci sull’analisi degli array di microfoni, essi presentano numerose applicazioni, come:
	Identificazione delle sorgenti sonore
	Isolamento delle sorgenti sonore
	Riduzione del rumore
	Miglioramento della qualità del suono
Prima di analizzare le varie tecniche di beamforming in questo ambito, è opportuno spostarsi su un accenno alle onde sonore per evidenziare le analogie con quelle elettromagnetiche e dunque le similitudini tra array di antenne e array di microfoni.

	Accenni alle onde acustiche
Le onde acustiche sono onde di pressione, ovvero la loro propagazione comporta una locale compressione e rarefazione del fluido in cui avviene tale propagazione. Esse soddisfano l’equazione delle onde del tipo
f\ =\ f(x\ -\ vt)
Tale equazione può essere scritta nella forma (qui semplificata per una sola coordinata spaziale):
\frac{d^2f}{dt^2}\ =\ v^2\frac{d^2f}{dx^2}
Nel caso delle onde acustiche quindi si ottiene l’equazione d’onda del tipo:
\mathrm{\nabla}^2p\ =\ \frac{1}{c^2}\frac{d^2p}{dt^2}
Dove p è la pressione, \mathrm{\nabla} è l’operatore Laplaciano e c è la velocità del suono nel fluido (≈ 340 m/s nell’aria).
Le sorgenti di onde sonore sono varie, e la più semplice di queste è la sorgente puntiforme detta monopolo. Se ci troviamo nello spazio libero, il monopolo emana onde acustiche sferiche. Ciò significa che in tutti i punti a uguale distanza dalla sorgente l’intensità del suono sarà la stessa, o, più nello specifico, il valore della grandezza fisica vibrante (la pressione) sarà uguale su tutti i punti della superficie della sfera considerata. Notiamo anche che l’energia totale rimane la stessa su tutti i fronti d’onda. Poiché però la loro superficie si estende allontanandosi dalla sorgente, essa si distribuisce su aree maggiori, pertanto l’intensità locale diminuisce.
 
Onda sferica che si propaga da una sorgente puntiforme


Le onde sferiche in forma armonica assumono la seguente forma:
p(r,\ t)\ =\ \frac{A}{r}cos(\omega t\ -\ kr)\ =\ \frac{A}{r}e^{j(\omega t\ -\ kr)}

	Array di sorgenti
Definiamo gli array come serie di sorgenti sonore, per poi spostarci su quelli di riceventi (microfoni). Come visto per gli array di antenne, gli array di sorgenti sonore possono assumere varie geometrie, tra cui le più diffuse sono:
	Lineare
	Circolare
	Sferica
Per i successivi passaggi assumeremo array lineari.
Prima di affrontare i concetti di interferenza e beamforming è importante precisare il concetto di near-field e far-field. Definiamo L la lunghezza totale dell’array, λ la lunghezza d’onda più elevata r la distanza dalla sorgente.
	Near-field (campo vicino) per \frac{L^2}{r\lambda} >> 1: il fronte d’onda è una sovrapposizione di fronti d’onda sferici ad andamento non ben definito; l’impedenza acustica è immaginaria e l’intensità sonora cala rapidamente per piccole variazioni di r.
	Far-field (campo lontano) per \frac{L^2}{r\lambda} << 1: il fronte d’onda si può approssimare come piano, l’impedenza acustica è principalmente reale e l’intensità sonora cala linearmente di 6 dB raddioppiando la distanza, quindi non ci sono grandi variazioni per piccole differenze di r.
Per studiare il comportamento degli array ci porremo in far-field, in modo da poter sfruttare utili approssimazioni altrimenti non applicabili.

 
Facciamo riferimento ad un array lineare in cui d è la distanza tra gli elementi, e tracciamo le congiungenti tra ogni elemento e il punto P in cui ci poniamo come osservatori. L’angolo α viene assunto uguale per tutti i segmenti poiché ci troviamo in far-field, mentre le differenze di cammino per giungere al punto P non sono trascurabili e vanno dunque calcolate dalla geometria dell’array. Nel nostro caso, se abbiamo N elementi nell’array, la distanza di cammino tra successivi è:
∆r = d sinα
A partire dall’equazione delle onde acustiche sferiche in forma armonica si può ottenere l’espressione del campo acustico totale emanato dall’array:
p(r,\ \alpha,\ t)\ =\ A(r)\ \frac{e^{jNkd\ sin\alpha}-1}{e^{jkd\ sin\alpha}-1}\ \bullet\ e^{j(\omega t-kr)}
L’array factor è dunque (normalizzato con massimo a 1):
AF\ =\ \frac{sin\left(\frac{Nkd}{2}sin\alpha\right)}{N\ sin\left(\frac{kd}{2}sin\alpha\right)}
Analizzando l’andamento dell’AF possiamo trovarne i minimi e i massimi, che corrispondono agli angoli α per cui si ha interferenza distruttiva o costruttiva. I massimi si trovano ponendo a 0 il denominatore, mentre i minimi ponendo a 0 il numeratore.
	Max: sinα = \frac{m\lambda}{d} con m = 0, ±1, ±2…
	Min: sinα = \frac{p\lambda}{Nd} con p = ±1, ±2 ma escludendo i valori di p che generano un punto di massimo.
Si deduce che tra ogni massimo ci sono N−1 minimi. Il massimo ottenuto per m = 0 viene detto main lobe, mentre gli altri vengono chiamati grating lobes e sono in genere indesiderati. È possibile dimensionare l’array in modo da avere solo il main lobe (array a singolo fascio) imponendo una condizione che viene detta spatial sampling in quanto è analoga al teorema del campionamento di Nyquist. Tale condizione impone che \frac{\lambda}{d}>1, ovvero d < λ.
È importante però notare che finora abbiamo lavorato con sorgenti in fase tra loro: se la fase relativa δ tra le sorgenti è diversa da 0, questo influenza la posizione del main lobe poiché il radiation pattern viene “slittato” di una quantità δ. In tal caso la condizione precedente deve tenere in considerazione la massima fase relativa possibile, pertanto il vincolo su d sarà più stringente, diventando:
d\ <\ \frac{\lambda}{2}

	Array di microfoni
Per quanto riguarda gli array di elementi riceventi (microfoni), le fondamenta del fenomeno fisico sono le stesse, con la differenza che l’approssimazione far-field è “al contrario”, ovvero le onde sono sferiche quando vengono emesse dalla sorgente in campo lontano e arrivano all’array di microfoni con fronti d’onda piani e paralleli.
Dalla differenza di cammino per giungere a due elementi consecutivi dell’array (prima calcolata) si può ottenere il rispettivo ritardo \tau=\frac{d}{c}sin\alpha, estendibile al ritardo tra due microfoni distanti n tra loro:
\tau_n=\ n\frac{d}{c}sin\alpha
È importante ricordare che a lato ricevente stiamo lavorando nel campo dell’audio digitale, perciò il segnale totale acquisito dall’array sarà la somma dei segnali acquisiti da ogni microfono, del tipo:
y(t)\ =\ \sum_{n\ =\ 1}^{N}{s(r_n,\ t)}
Analizziamo ora varie tecniche di beamforming, a partire dalle più semplici e immediate alle più recenti e complesse.

	Delay-and-sum beamforming
Viene detto anche beamforming classico, poiché è il più vecchio e semplice metodo per indirizzare l’ascolto dei microfoni verso una specifica direzione. Sfruttando la dipendenza tra la direzione da cui proviene il segnale e il ritardo con cui esso arriva a ogni microfono, si può calibrare la fase dei microfoni con un filtro FIR digitale in modo da compensare questi ritardi e fare in modo che i segnali si sommino in fase per una certa direzione, amplificandone l’intensità, attenuando grazie all’interferenza distruttiva quelli provenienti da altre direzioni. Il segnale totale è quindi:
y(t)\ =\ \sum_{n\ =\ 1}^{N}{w_n\ s(r_n,\ t\ -\tau_n)}

I termini w_n sono i pesi dei segnali, poiché si può decidere di accentuare in particolare i segnali registrati da certi microfoni. La limitazione di questa tecnica è che ha buone prestazioni per segnali a banda stretta, ma a causa della dispersione cromatica la performance peggiora all’aumentare della banda del segnale.
Una soluzione che ovvia a questo problema è quella di sostituire i pesi w_n, reali e costanti, con dei filtri FIR, che gestiscono meglio la risposta in frequenza. Si ottiene così il filter-and-sum beamforming, che può essere visto come un’estensione del delay-and-sum beamforming.

	Constant-Beamwidth microphone array
La beamwidth del main lobe dell’array, ovvero la larghezza del fascio a metà altrezza, si trova imponendo {|AF|}^2=0,5. Se ne deduce che essa è inversamente proporzionale alla frequenza di lavoro, perciò ad alte frequenze abbiamo un main lobe molto stretto, e possono inoltre comparire i grating lobes. Per evitare ciò, e avere quindi una beamwidth costante indipendentemente dalla frequenza, si utilizzano degli array di microfoni al cui interno sono innestati dei sub-array, ognuno dei quali ha una spaziatura diversa tra gli elementi ed è perciò progettato per gestire range di frequenze diversi.

	Differential microphone arrays
Gli array di microfoni differenziali, o DMA, ricadono nella categoria filter-and-sum e adottano un approccio più avanzato dei delay-and-sum in quanto consentono di posizionare a piacere le direzioni di massimo e di minimo, consentendo performance migliori delle precedenti. Nel delay-and-sum infatti è possibile decidere la direzione di massimo, ma quelle di minimo sono dettate solo dalla geometria dell’array e non modificabili.
I DMA, grazie al fatto che due microfoni adiacenti ricevono il segnale con un ritardo, approssimano la derivata del segnale eseguendo la differenza tra questi due segnali. Ne segue che avendo N microfoni si può approssimare la derivata fino all’ordine N−1. Per questo motivo i DMA sopprimono molto bene i rumori di fondo e sono molto sensibili a cambiamenti repentini nel segnale.

 

	Eigenbeamforming arrays
Una geometria molto utilizzata, oltre a quella lineare, è quella degli array sferici, in cui i microfoni sono posti sulla superficie di una sfera rigida. In questo modo viene misurata la pressione acustica in ogni punto in cui è situato un microfono, per poi trasformare il campo sonoro in uno spazio di coordinate sferiche. Questo spazio è formato da modalità ortonormali tra loro dette eigenbeams, e possono essere comprese meglio con un’analogia con i modi naturali per un sistema meccanico: forniscono infatti una completa rappresentazione del campo originale sotto forma di armoniche sferiche, e si combinano tra loro senza sovrapporsi.
Dopo aver ottenuto gli eigenbeams, essi vengono sottoposti a un weight-and-sum beamforming, in cui vengono scalati e sommati tra loro.

	Adaptive arrays
Finora abbiamo visto array di microfoni la cui risposta rimane statica, poiché una volta tarati i pesi dei segnali essi restano fissi. Questo approccio funziona se la conoscenza a priori dell’ambiente acustico è sufficientemente simile a quella  effettiva, ma in caso di cambiamenti dinamici nei segnali e nel rumore è utile sfruttare un approccio dinamico.
Tale approccio equivale a un’auto-ottimizzazione dell’array a partire da certi vincoli imposti: il vincolo più comune è quello di minimizzare il SNR (signal-to-noise ratio), in modo da avere alta amplificazione del segnale e alta attenuazione dei rumori indesiderati. In questo modo la progettazione dell’array diventa un problema di ottimizzazione sotto vincoli.
