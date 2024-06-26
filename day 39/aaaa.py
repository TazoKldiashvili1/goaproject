
originaluri_pasi = float(input("Enter the original price of the product: "))

pasdaklebis_procentuloba = float(input("Enter the discount percentage: "))

pasdaklebis_raodenoba = (pasdaklebis_procentuloba / 100) * originaluri_pasi

new_price = originaluri_pasi - pasdaklebis_raodenoba

print("axali pasi yvelapris shemdeg aris " + str(pasdaklebis_procentuloba) + "% pasdakleba aris: $" + str(round(new_price, 2)))



