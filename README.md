# Opetussovellus

Tämän työn aiheena on Opetussovellus. 
Tämän sovelluksen tarkoituksena on olla Moodle-tyylinen alusta, johon on mahdollista lisätä
kursseja, niihin on mahdollista rekisteröityä, sekä niissä olevia materiaaleja voida käyttää opiskeluun.
Sovellukseen tulee ainakin seuraavat ominaisuudet:

- Kaikille on mahdollista tehdä:
  - sisään- ja uloskirjautuminen
- Opiskelijaksi kirjautunut pystyy tekemään seuraavia asioita:
  - kurssilistaus, kursseihin liittyminen
  - kurssien materiaalien lukeminen 
  - kurssien tehtävien ratkominen (monivalinta, tekstikenttävastaus)
  - tietoa omista ratkaistuista tehtävistä\
- Opettajaksi kirjautunut pystyy lisäksi tekemään seuraavia asioita:
  - luoda, muokata ja poistaa kursseja
  - lisätä kurssialueelle tehtäviä ja materiaalia
  - näkemään opiskelijoiden tiedot ja heidän ratkaistut tehtävät

8.8.2021:
Tällä hetkellä sovelluksessa on toteutettuna seuraavat ominaisuudet:
- Sisään- ja uloskirjautuminen
- Rekisteröityminen
- Kurssien lisääminen (opettajana)
- Kurssien poistaminen (opettajana)
- Kurssien katseleminen

Sovellus on testattavissa osoitteessa:
http://opetussovellus.herokuapp.com/
Sovellusta voi tällä hetkellä testata parhaiten rekisteröitymällä opettajana, ja kokeilemalla lisätä ja poistaa kursseja.

TO-DO:
- Kurssien tehtävien lisääminen (opettajana)
- Kursseille liittyminen (opiskelijana)
- Tehtävien ratkaiseminen
- Tiedot ratkaistuista tehtävistä

22.8.2021:
Tällä hetkellä sovelluksessa on toteutettuna seuraavat ominaisuudet:
- Sisään- ja uloskirjautuminen
- Rekisteröityminen
- Kurssien lisääminen (opettajana)
- Kurssien poistaminen (opettajana)
- Kurssien katseleminen

- Tehtävien lisääminen (opettajana)
- Tehtävien poistaminen (opettajana)
- Tehtävien ratkaiseminen
- Kursseille liittyminen

Sovellus on testattavissa osoitteessa:
http://opetussovellus.herokuapp.com/
Sovellusta voi tällä hetkellä parhaiten testata rekisteröitymällä opettajana, ja kokeilemalla lisätä ja poistaa kursseja, sekä
lisätä ja poistaa tehtäviä eri kursseille. Tällä hetkellä opettajana voi myös ratkaista tehtäviä, ja saada tiedon onko vastaus oikein.
Profiilisivun tiedot ja sovelluksen ulkoasu ovat vielä kesken.

TO-DO:
- Profiilisivun korjaus
- Profiilisivulle datapointtien lisääminen (esim. %-oikeat vastaukset, kurssilistaus) 
- Sovelluksen ulkoasun korjaus
- Tehtävien ratkaisu vain oppilaille

5.9.2021.
Valmiissa sovelluksessa on toteutettuna seuraavat ominaisuudet:
- Sisään- ja uloskirjautuminen
- Rekisteröityminen
- Kurssien lisääminen (opettajana)
- Kurssien poistaminen (opettajana)
- Tehtävien lisääminen (opettajana)
- Tehtävien poistaminen (opettajana)
- Tehtävien ratkaiseminen ja vastauksen tarkistus
- Kursseille liittyminen
- Kursseilta poistuminen
- Ulkoasu bootstrapilla
- Oikean käyttäjäroolin ja csrf tarkistus
- Profiilisivu, joka päivittyy kurssien ja tehtävien poistamisen/lisäämisen mukaisesti

Sovellus on testattavissa osoitteessa:
http://opetussovellus.herokuapp.com/

Sovellusta voi parhaiten testata rekisteröitymällä opettajana, kokeilemalla lisätä ja poistaa kursseja, sekä lisätä ja poistaa tehtäviä
eri kursseille. Kursseille voi myös ilmoittautua ja poistaa ilmoittautumisen. Lisätessä ja poistaessa kursseja ja tehtäviä voi
seurata profiilisivun päivittymistä.
