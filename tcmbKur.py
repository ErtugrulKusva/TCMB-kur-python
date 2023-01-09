import pandas as pd
xml_url="https://www.tcmb.gov.tr/kurlar/today.xml"
df = pd.read_xml(xml_url)
dfUSD=df.query('Kod == "USD"')
dfEUR=df.query('Kod == "EUR"')
usdSatis=float(dfUSD["BanknoteSelling"])
eurSatis=float(dfEUR["BanknoteSelling"])
print("usdSatis:",usdSatis, "-- eurSatis:",eurSatis)

