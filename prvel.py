with open('txs_data.csv', 'w', encoding='utf-8') as f:
    # Write data to the file
    f.write('Transaction ID,Amount,Date,Description\n')
    for tx in txs:
        f.write(f'{tx.id},{tx.amount},{tx.date},{tx.description}\n')
