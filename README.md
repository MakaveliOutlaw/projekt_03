# Elections Scraper

Jedná se o Python skript, který scrapuje výsledky voleb do Poslanecké sněmovny ČR z roku 2017.
Stahuje data z jednotlivých obcí ve vybraném územním celku.
Výsledky ukládá do souboru CSV.

# Pokyny k instalaci

1. Vytvoření virtuálního prostředí:
   
   python -m venv venv
   
2. Aktivace virtuálního prostředí:
   - **Windows:**
     
     venv\Scripts\activate
     
   - **Linux/macOS:**
     
     source venv/bin/activate
     
3. Přehled potřebných knihoven je uložen v souboru `requirements.txt`, k jejich instalaci slouží následující příkaz:
   
   pip install -r requirements.txt

# Spuštění skriptu

Ke spuštění jsou vyžadovány 2 agrumenty:

1. **URL adresa vybraného územního celku** — odkaz na stránku se seznamem obcí naleznete zde: https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ, pomocí odkazů ve sloupci Výběr okrsku - symbol X.

2. **Název výstupního souboru** — soubor, kam se uloží výsledky ve formátu .csv (např. vysledky_hradec_kralove.csv)

Ukázka:

python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201" vysledky_hradec_kralove.csv

# Výstup

V souboru CSV jsou obsaženy tyto informace:

- **Kód obce**
- **Název obce**
- **Voliči v seznamu**
- **Vydané obálky**
- **Platné hlasy**
- **Kandidující strany** 




