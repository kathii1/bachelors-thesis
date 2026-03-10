## Projektbeschreibung

Dieses Repository enthält den Programmcode zu meiner Bachelorarbeit (Stand: April 2023)  
**„Das Diskrete Logarithmusproblem und kryptographische Anwendungen“**.

Die Arbeit behandelt das diskrete Logarithmusproblem (DLP) und zeigt, wie es als sicherheitskritische Grundlage in verschiedenen kryptographischen Verfahren eingesetzt wird, unter anderem im Diffie–Hellman-Schlüsselaustausch, in der ElGamal-Verschlüsselung und in der Schnorr-Signatur. Die hier enthaltenen Skripte implementieren verschiedene Algorithmen zur Lösung des DLP und ermöglichen einen experimentellen Vergleich ihrer Laufzeiten.

Implementierte Algorithmen:

- **Pohlig–Hellman-Algorithmus** (`pohligHellman.py`)  
- **Shanks’ Baby-step–Giant-step-Algorithmus** (`babystepGiantstep.py`)  
- **Pollard-ρ-Algorithmus** (`pollardRho.py`)  
- **Pollard-ρ-Algorithmus in Kombination mit Pohlig–Hellman** (`pollardRhoPH.py`)  
- **Indexkalkül-Methode** (`indexCalculus.py`)  
- **Indexkalkül-Methode in Kombination mit Pohlig–Hellman** (`indexCalculusPH.py`)  

Die Algorithmen werden für geeignete Gruppen implementiert, auf konkrete Instanzen des DLP angewendet und im Hinblick auf ihre praktische Laufzeit verglichen.

## Quellen
Der Code basiert auf den Konzepten dieser beiden Quellen: 
- Johannes Buchmann. Einführung in die Kryptographie. 6. Aufl. Springer Spek
trum, 2016.
- Robert Granger, Thorsten Kleinjung und Jens Zumbrägel. “Indiscreet loga
rithms in finite fields of small characteristic”. In: arXiv preprint arXiv:1604.03837
(2016).

