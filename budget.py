class Category():

  def __init__(self,name):
    try:
      name = name.lower()
    except:
      print('Invalid category item')
    self.name = name
    # Create instance of the ledger for this category
    self.ledger = list()

  def get_balance(self,spent=False):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    neg = 0
    if spent:
      for item in self.ledger:
        if item["amount"] < 0:
          neg += -1*item["amount"]
      return neg
    return balance
  
  def check_funds(self,amount):
    balance = self.get_balance()
    if amount > balance:
      return False
    else:
      return True
  
  def deposit(self,amount,desc=''):
    self.depo = dict()
    self.depo["amount"] = amount
    self.depo["description"] = desc
    self.ledger.append(self.depo)

  def withdraw(self,amount,desc=''):
    if self.check_funds(amount):
      self.withd = dict()
      self.withd["amount"] = -1*amount
      self.withd["description"] = desc
      self.ledger.append(self.withd)
      return True
    else:
      return False
  
  def transfer(self,amount,receiving):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to "+receiving.name.capitalize())
      receiving.deposit(amount,"Transfer from "+self.name.capitalize())
      return True
    else:
      return False

  # Create Visual Ledger
  def __str__(self):
    # Create Header (Length = 30 char)
    header = '*'*15+self.name.capitalize()+'*'*15
    while len(header) > 30:
      header = header[1:-1]

    ledger = header+'\n'

    # Set up and create line item transactions
    lineitem = ''
    for trans in self.ledger:
      desc = trans['description']
      amount = str(trans['amount'])
      # Format monetary value
      if '.' not in amount:
        amount += '.00'
      lineitem = desc+' '+amount
      while len(lineitem) > 30:
        desc = desc[:-1]
        lineitem = desc+' '+amount
      while len(lineitem) < 30:
        desc = desc+' '
        lineitem = desc+' '+amount
      ledger += lineitem+'\n'
    
    # Retrieve total balance remaining in category
    total = self.get_balance()
    total = "Total: "+str(total)
    ledger += total
    print(ledger)
    
    return ledger

    
# Histogram Chart of Transactions
def create_spend_chart(category):
  cat_list = category
  try:
    category = list(cat_list)
  except:
    print("Input must be a list.")
  if len(cat_list) > 4:
    print('Input list cannot be more than four categories.')

  # Retrieve balances
  spent = []
  cat = []
  for items in cat_list:
    cat.append(items.name.capitalize())
    spent.append(items.get_balance(spent=True))

  # Calculate Spending Proportions
  overallex = sum(spent)
  prop = []
  for val in spent:
    prop.append(val/overallex)
  
  # Convert Proportion to Percentage
  prop = [val*100 for val in prop]

  # Create Spend Spending Chart
  chart = 'Percentage spent by category'
  for percent in range(100,-10,-10):
    chart += '\n'
    if percent == 100:
      chart += str(percent)+'| '
    elif percent < 100:
      chart += (str(percent)+'| ').rjust(5)
    else:
      chart += (str(percent)+'| ').rjust(5)
  
  # Evaluate spending proportion to chart
    for val in range(len(prop)):
      try:
        if prop[val] >= percent:
          chart += 'o  '
        else:
          chart += '   '
      except:
        pass
  chart += '\n'

  # Bottom Axis
  xis = '-'+'---'*len(cat)
  chart += xis.rjust(len(xis)+4)+'\n'
  
  # Category Label
    # Determine maximum letters
  maxword = max(cat,key = len)
  label = ''
  count = 0
  for l in range(len(maxword)):
    label += '    '
    for word in cat:
      try:
        label += ' '+word[l]+' '
      except:
        label += '   '
    if count == len(maxword)-1:
      label += ' '
    else:
      label += ' \n'
      pass
    count += 1

  # Format Category Labels
  chart += label
  print(chart)
  print(len(chart))
  return chart
