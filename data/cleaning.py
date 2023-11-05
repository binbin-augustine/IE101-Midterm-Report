def cleaning(filthy:list[str]) -> dict[str,int] :
    filthy = [entry.strip().split(",") for entry in filthy]
    
    clean = {
        entry[0].lower() : entry[1] for entry in filthy
    }
    return clean


with open('data/Golomt_2016.csv', 'r') as Golomt: 
    contents_golomt = cleaning(Golomt.readlines())

with open('data/Khan_2016.csv', 'r') as Khan: 
    contents_khan = cleaning(Khan.readlines())

with open('data/State_2016.csv', 'r') as State: 
    contents_state = cleaning(State.readlines())

with open('data/TDB_2016.csv', 'r') as Tdb: 
    contents_tdb = cleaning(Tdb.readlines())

with open('data/Xac_2016.csv', 'r') as Xac:
        contents_xac = cleaning(Xac.readlines())

Banks = {'Golomt': contents_golomt, 
         'Khan': contents_khan, 
         'State': contents_state, 
         'TDB': contents_tdb, 
         'Xac': contents_xac}

input_variable = ["Fixed Asset", "Equity", "Operating Expenses", "Interest Expenses", "Impaired Loan", ]
output_variable = ["Gross Loan", "Total Deposits", "Investment", "Operating Income", "Non-interest Income"]

with open('data/combined_2016.csv', 'w') as combined:
    combined.write( 'Banks,' + ','.join(input_variable) + ',' + ','.join(output_variable) + '\n')
    for bank, inside in Banks.items():
        combined.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(bank, 
                                          inside['fixed assets'], 
                                          inside['total equity'], 
                                          inside['other operating expense'], 
                                          inside['interest expense'],
                                          inside['non-performing loans'],
                                          inside['loan (net)'],
                                          inside['savings'],
                                          inside['investments'],
                                          inside['other income'],
                                          inside['non-interest income']))

print(combined)
