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

# Ukázka výstupu v souboru CSV:

Kód obce	Název obce	Voliči v seznamu	Vydané obálky	Platné hlasy	
569828	Babice	165	109	108	
569836	Barchov	227	141	140	21
569852	Běleč nad Orlicí	269	207	206	38	
569861	Benátky	93	67	67	9	
569879	Blešno	322	227	227	53	
569887	Boharyně	470	297	297	20	
569917	Černilov	1901	1234	1226	150	

# Výstupu v terminálu

✅ Načteno 104 obcí.

✅ Výsledky uloženy do vysledky_hradec_kralove.csv
