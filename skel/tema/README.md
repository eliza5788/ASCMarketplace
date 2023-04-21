Nume: Codescu Elisabeta Maria
Grupă: 331AC

# Tema 1 Marketplace

Organizare
-
1. Explicație pentru soluția aleasă:

* Pentru a rezolva tema, am folosit scheletul oferit ca suport pe https://gitlab.cs.pub.ro/asc/asc-public/-/tree/master/assignments/1-marketplace.

* Am implementat exact clasele marketplace, producer și consumer din schelet, plus modulul product.py, neconsiderând necesar să generez alte clase suplimentare. De asemenea, am dezvoltat strict metodele deja incluse în schelet, nu am mai definit altele in plus. 
* În ceea ce privește structurile de date necesare păstrării informațiilor, cele adăugate de mine au fost:
* În Marketplace:
- două variabile de tip int care țin contorul numărului de producători și de coșuri de cumpărături, acestea fiind relevante mai ales pentru definirea producer_id și cart_id în producer.py, respectiv consumer.py
- un dicționar care ține evidența tuturor producătorilor din marketplace împreună cu produsele acestora - key-ul îl reprezintă producer_id, iar value îl reprezintă lista de produse ale acestuia
- un alt dicționar care ține evidența tuturor coșurilor de cumpărături- key-ul îl reprezintă lista de produse alese și producătorul corespunzător fiecăruia
* Am protejat zonele  din **register_producer** și **new_cart** cu ajutorul unui lock.

* 2. Consideri că tema este utilă?

* Personal, mie mi s-a părut extrem de utilă aceasta temă; fiind de la Ingineria Sistemelor, nu am mai lucrat până acum cu Python la acest nivel. Am considerat inițial o provocare implementarea elementelor de threading, însă laboratoarele și researchul pe internet m-au ajutat să mă lămuresc. 

* Consideri implementarea naivă, eficientă, se putea mai bine?

* Cred că implementarea este destul de eficientă, având în vedere că sunt începătoare în Python. Evident, probabil se putea să implementez și mai bine de atât :) 


Implementare
-
* Am implementat întregul enunț al temei, cu excepția unittest și logging, deoarece nu sunt suficient de sigură cum să le folosesc, și nu am vrut să îmi afecteze cumva rezultatul testelor rulate pe codul simplu. 
* Nu am utilizat funcții extra și nu există funcționalități lipsă.

* Lucruri interesante descoperite pe parcurs și dificultăți întâmpinate:

* Inițial, am considerat că nu este necesar să folosesc vreun lock, însă după mai multe ore petrecute documentându-mă pe tema acestuia, l-am implementat în zonele specificate mai sus din fișierul marketplace.py.
* Mi s-a parut foarte interesant să descopăr despre existența dicționarelor în Python, care nu există în limbajul C. Mi s-a parut interesantă distincția dintre liste, tupluri și dicționare.
* Pylint a fost util pentru că am reușit să-mi formatez codul mult mai eficient cu ajutorul său, 
* nu l-am mai folosit până acum și mi s-a parut chiar ingenios.


Resurse utilizate
-

* Resurse utilizate - 

* https://ocw.cs.pub.ro/courses/asc/laboratoare/01
* https://ocw.cs.pub.ro/courses/asc/laboratoare/02
* https://ocw.cs.pub.ro/courses/asc/laboratoare/03
* https://gitlab.cs.pub.ro/asc/asc-public/-/tree/master/assignments
* https://www.w3schools.com/python/ref_dictionary_update.asp
* https://realpython.com/python-dicts/
* https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
* https://www.programiz.com/python-programming/list
* https://www.w3schools.com/python/python_tuples.asp


Git
-
1. https://github.com/eliza5788/ASCMarketplace.git
