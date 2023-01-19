#Money change Algorithm

def optimal_change(cost, paid):
  
  if paid == cost: #If no change
    return f'The optimal change for an item that costs ${cost} with an amount paid of ${paid} is no change given.'
  
  if paid < cost: #If paid less than cost
    return 'Not enough money for this item.'
  
  change = paid - cost 
  
  bills = { 
    '100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '1': 0, 'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0
         }
  
  def change_update(key, value, change):
    bills[key] += 1
    change = round(change - value, 2)
    return change
      
  while (change > 0): # update bills dict to match the change
    if change > 100:
      change = change_update('100', 100.00, change)
      continue
    if change >=  50:
      change = change_update('50', 50.00, change)
      continue
    if change >=  20:
      change = change_update('20', 20.00, change)
      continue
    if change >=  10:
      change = change_update('10', 10.00, change)
      continue
    if change >=  5:
      change = change_update('5', 5.00, change)
      continue
    if change >=  1:
      change = change_update('1', 1.00, change)
      continue
    if change >=  .25:
      change = change_update('quarter', 0.25, change)
      continue
    if change >=  .1:
      change = change_update('dime', 0.10, change)
      continue
    if change >=  .05:
      change = change_update('nickel', 0.05, change)
      continue
    if change >  0:
      change = change_update('penny', 0.01, change)
      continue
   
  return optimal_bills(bills, cost, paid)

#Optimal bills Algorithm

def optimal_bills(bills, cost, paid):
  
  str = ''
  msg = f'The optimal change for an item that costs ${cost} with an amount paid of ${paid} is '
  
  for k, v in bills.items(): #key: value pairs
    if len(k) <= 3: #all the bills
      if v == 1:  #if only 1 bill
        msg += f'{v} ${k} bill, '
        continue
      if v >= 2:  #if 2 or more bills
        msg += f'{v} ${k} bills, '
        continue
    else: #all the change
      if k == 'penny': #fix the penny -> pennies problem
        if v >= 2: #if 2 more pennies
          msg += f'{v} {k[:-1]}ies, '
          continue
      if v == 1: #if single coin
        msg += f'{v} {k}, '
        continue
      if v >= 2: #if multiple of the same coin
        msg += f'{v} {k}s, '
  #fixing the final ', and ' problem and adding a '.' at the end of string
  str = msg[-15:]
  str = str[:-2] + '.'
  str = str.replace(', ', ', and ')
  msg = msg[:-15] + str
       
  return msg