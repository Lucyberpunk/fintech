#!/usr/bin/env python
# coding: utf-8

# <span class="alert alert-success" style="display: block;">
#     
# ## FNCE90084: Fintech: Foundations and Applications - Assignment 1: Blockchain and Smart Contracts
# 
# </span>
# 
# <span class="alert alert-info" style="display: inline-block;">
# All questions must be completed and submitted via Jupyter Hub (any other submissions will not be
# marked). The assignment notebook contains certain pre-defined variables. A submission that renames these
# variables will attract zero marks. Calculations involving decimal numbers should be precise till 3 decimal
# places (e.g., if answer is 4.122229, then one should use 4.123 instead of 4.1). Your submitted code snippets are expected to run correctly on first execution despite the asynchronous
# nature of the blockchain interactions. 
# 
# This notebook provides cells where you can enter your solutions.
# 
# <span class="label label-danger text-uppercase">Note</span>: You are *not* allowed to use `sleep` or any other methods to slow down execution. 
# Please use the **ED** forum to ask any queries regarding this assignment. 
# 
# **Late submission penalties**
# - 10% of the maximum mark per day the assessment task is overdue (where work is less than a week overdue);
# - Assignments submitted 10 days after the deadline will not be graded and will receive a grade of zero.
# - Exceeding word limits: Assessment tasks should not vary more than 10% from the required word count (where relevant).
# 
# **Assignment Extensions**
# - Faculty extensions policy can be found here: [http://policy.unimelb.edu.au/MPF1326#section-4.37](http://policy.unimelb.edu.au/MPF1326#section-4.37)
# - Requests for an assignment extension should be submitted here: [http://go.unimelb.edu.au/yh9n](http://go.unimelb.edu.au/yh9n)
# 
# **Submission**
# This assignment should be submitted via the JupyterHub system. 
# 
# **Plagiarism declaration**
# By submitting work for assessment I hereby declare that I understand the University's policy on academic integrity and statement on the use of artificial intelligence software. In accordance with these documents, I declare that the work submitted is original and solely my work, and that I have not been assisted by a third party (collusion) apart from where the submitted work is for a designated collaborative task, in which case the individual contributions are indicated. I also declare that I have not used any writing tools or sources without proper acknowledgement (plagiarism). Where the submitted work is a computer program or code, I further declare that any copied code is declared in comments identifying the source at the start of the program or in a header file, that comments inline identify the start and end of the copied code, and that any modifications to code sources elsewhere are commented upon as to the nature of the modification.
#     
# <hr/>
#     
# **Important:** It is important that you follow the assignment submission instructions as per "How to submit assignments on JupyterHub" available under Modules/Assessment on Canvas. 
# 
# <span class="label label-danger text-uppercase">Note</span>: The assignment will ask you to follow certain precise instructions such as storing results in predefined variable names, or reading CSV files into dataframes with specific names. Failure to follow these instructions would attract penalty.
# </span>
# 
# <span class="alert alert-danger"  style="display: inline-block;">
#     <span class="label label-danger text-uppercase">Note</span>
#     <span>
#         Write your answers in <strong>this notebook</strong> only <em>within</em> the provided cells. <em>Do not</em> create additional cells or duplicate/copy existing cells. <br/>
#         You may keep a copy of this base notebook as reference to original file and to compare that you haven't accidentally added cells, duplicated cells or changed the order of these cells. However, note that additional notebooks and copies aren't marked. 
#     </span>
# </span>

# ### Predefined Package Imports

# In[1]:


"""Import Required Libraries - No need to duplicate or reimport; 
This is a Read-Only cell. Simply execute this cell"""

# Import the bmmnet library
from bmmnet import *

# Import the matplotlib library, used for plotting
import matplotlib.pyplot as plt
import seaborn as sns 

# Import the numpy library, used for numerical functions
import numpy as np


# ### Import your additional packages in the cell below
# Further imports are not required, but you may use additional packages if you wish.

# In[2]:


"""Your own additional imports go here"""
# BEGIN - YOUR CODE GOES HERE
import pandas as pd
pass
# END - YOUR CODE GOES HERE


# ### Contract Addresses

# In[3]:


"""Predefined Variables - Do Not Change their Name and Value;
This is a Read-Only cell. Remember to execute this cell once"""
bmmcoin_address = get_bmmcoin_address()
bmm_market_address = get_market_address()

print(f"BMM Coin is at {bmmcoin_address}")
print(f"BMM Market is at {bmm_market_address}")


# ## Question 1 [2 marks]
# 
# <strong> Q1 (i) [<font color="red"> 0 marks </font>]</strong> Create a connection object to the blockchain network, and store a public address and private key for the BMM Ethereum blockchain. You should use these account details for completing this assignment. You should use an existing account that has enough ether to pay for the transactions.
# 
# <span class="label label-danger text-uppercase">Note</span>: You should *not* create a new account in the cell below.

# In[4]:


"""Predefined Variables - Do Not Change their Name;
This is a Read-Only cell. Remember to execute this cell once"""
node_connection = None

# Save address and private key as variables
address = ""
private_key = ""


# In[5]:


"""Populate the variables shown above with appropriate values here"""
# BEGIN - YOUR CODE GOES HERE

node_connection = None

# Create a connection to the blockchain network
node_connection = connect()

# Save address and private key as variables
address = "0x7E24CaA3eB73d8ce13dA1C1f05027E6F178371fb"
private_key = "19a8ecee2376baf4ba6763dc10a8f913efad2f650dab76b5eb9a9fe19f18ab05"

pass
# END - YOUR CODE GOES HERE


# <strong> Q1 (ii) [<font color="red"> 0.5 marks </font>]</strong> Request the amount of BMM Coins required to purchase product `C` from the system. You should store the transaction hash (in hex) in the pre-defined variable. You should not hard code the transaction hash.

# In[6]:


"""Predefined Variables - Do Not Change their Name;
This is a Read-Only cell. Remember to execute this cell once"""
bmm_request_hash = None


# In[7]:


"""Populate the variables shown above with appropriate values here"""
# BEGIN - YOUR CODE GOES HERE

#request money
request_ether(address, 500000) #request someone to send 500000

market_contract = get_market_contract(node_connection) #create variable that stores the details of the market contract
products = market_contract.functions.getProducts().call() # this product is a list

fees={}
#write a loop 
for product in products: 
    fees[product] = market_contract.functions.getFee(product).call()

nonce = node_connection.eth.get_transaction_count(address) # get the nonce
amount = fees['C'] # specify amount of bmm coints that we want to receive to buy product C

#stores the information/detail of the smart contract that we try to interact with
coin_contract = get_bmm_contract(node_connection) 

#specify the params of the transaction = a dictionary of other details
bmm_request_data = {"from": address, "nonce": nonce, "gas":100000, "gasPrice": 1} 

# buidling the transaction by this syntax: object_name.functions.function_name().method_name() 
bmm_request = coin_contract.functions.request(amount).build_transaction(bmm_request_data) 

signed_bmm_request = node_connection.eth.account.sign_transaction(bmm_request, private_key=private_key) # sign the transaction
bmm_request_hash = node_connection.eth.send_raw_transaction(signed_bmm_request.rawTransaction)

# Convert our hash into hexadecimal format and print it out
bmm_request_hash = to_hex(bmm_request_hash)
print(bmm_request_hash)

# END - YOUR CODE GOES HERE


# In[8]:


"""Do not remove this cell."""


# <strong> Q1 (iii) [<font color="red"> 1.5 marks </font>]</strong> Buy product "C" from BMM Market. You should store the transaction hash (in hex) for your transaction in the pre-defined variable. You should not hard code the transaction hash.

# In[9]:


"""Predefined Variables - Do Not Change their Name;
This is a Read-Only cell. Remember to execute this cell once"""
buy_product_hash = None


# In[10]:


"""Populate the variables shown above with appropriate values here"""
# BEGIN - YOUR CODE GOES HERE

#Approving Market contract to withdraw BMM Coins
nonce += 1 # get the nonce
fee = fees['C'] # fee for product C
market_address = get_market_address() #specifies the market address of the smart contract 


allow_product_data = {"from": address, "nonce": nonce, "gas":150000, "gasPrice": 1}
allow_product = coin_contract.functions.approve(market_address, fee).build_transaction(allow_product_data) #get approve to deduct how many coins if the market address ask for them, if others ask do not send

signed_allow_product = node_connection.eth.account.sign_transaction(allow_product, private_key=private_key) # sign the transaction 

allow_product_hash = node_connection.eth.send_raw_transaction(signed_allow_product.rawTransaction) # Send the signed transaction to the network

allow_product_hash = to_hex(allow_product_hash)

#Purchasing product from BMM Market contract.
nonce += 1 # get the nonce
product = 'C'# product to buy
buy_product_data = {"from": address, "nonce": nonce, "gas":150000, "gasPrice": 1}
buy_product = market_contract.functions.buyProduct(product).build_transaction(buy_product_data)

signed_buy_product = node_connection.eth.account.sign_transaction(buy_product, private_key=private_key) # sign the transaction 

buy_product_hash = node_connection.eth.send_raw_transaction(signed_buy_product.rawTransaction) # Send the signed transaction to the network

# Convert our hash into hexadecimal format and print it out
buy_product_hash = to_hex(buy_product_hash)
print(f"The hash of the buy transaction is {buy_product_hash}")

# END - YOUR CODE GOES HERE


# In[11]:


"""Do not remove this cell."""


# ## Question 2 [3 marks]
# 
# <strong> Q2 (i) [<font color="red"> 1 marks </font>]</strong> Complete the function `get_purchase_details(tx_hash)`. The function should take a transaction hash and return either: 
# - `dict`: This should include details of the purchase (e.g., the product and who purchased it). See the function comments for details.
# - `None`: If the given transaction hash is not for buying a product.
# 
# Your function should not throw any error. You can assume only hashes of existing transactions will be passed to the function.

# In[12]:


def get_purchase_details(tx_hash):
    """
    Returns a dictionary with relevant data of the purchase.
    Example 1:
    {'from': '0xf69c049d2482264de6556357b32145F63224c44a', 'product': 'A'}
    
    Example 2:
    {'from': '0x62e1098963f1fB66c8342EF288BEF464030aC761', 'product': 'B'}
    
    """
    # BEGIN - YOUR CODE GOES HERE
    
    #get the transaction details
    tx=node_connection.eth.get_transaction(tx_hash)

    try:
        function_name, function_inputs = market_contract.decode_function_input(tx["input"])
        
         #check if the given transaction hash is not for buying a product
        if function_name.fn_name == "buyProduct":

            #get the purchaser's detail
            detail_from = tx['from']

            #get the product name
            prod_name = function_inputs['product']

            #create the dictionary
            dictionary = {
            "from": detail_from,
            "product": prod_name,
            }

            return dictionary

        else:
            return None
        
    except ValueError:
        return None  # ValueError occurred   

#check the function
result1 = get_purchase_details(bmm_request_hash)
result2 = get_purchase_details(buy_product_hash)
result3 = get_purchase_details(0x921c72de895878b8ca5d6377b71e1d98f680bada30dd340903aef394d6c3c004)

print(result1)
print(result2)
print(result3)

pass
    # END - YOUR CODE GOES HERE


# In[13]:


"""Do not remove this cell."""


# <strong> Q2 (ii) [<font color="red"> 2 marks </font>]</strong> Write a loop that retrieves purchase details from the blockchain for the relevant transactions stored between blocks numbers **184** and **190** (inclusive). You should use the function
# `get_purchase_details(tx_hash)` from the previous question. 
# 
# We will assume that product fees do not change within a block. You should also use the following data structure for storing the information. 
# 
# ```python
# data = {
#     N: {
#         'buys': {'X': number of transactions for purchasing product 'X' in block with number N},
#         'fee':  {'X': fee for product 'X' in block with number N}
#     }
# }
# ```        
# 
# The `data` variable stores the number of product purchase transactions with respect to blocks. For example if there were `10` transactions for product `A` in block number `100` (`N=100`), then `data[100]['buys']['A']` should store the value `10`. If the fee for product `A` in block `100` was `2` BMM Coins, then `data[100]['fee']['A']` should store the value `2`.
# 
# <span class="label label-danger text-uppercase">Note</span>: Failure to use the provided data structure will result in 0 marks for this part. The code may take some time to run.
# 

# In[14]:


"""Predefined Variables - Do Not Change their Name;
This is a Read-Only cell. Remember to execute this cell once"""
start_block = 184
end_block = 190

data = {}


# In[15]:


"""Populate the variables shown above with appropriate values here"""
# BEGIN - YOUR CODE GOES HERE

"""
"""

start_block = 184
end_block = 190

r_data = []  # Initialize a list to store transaction data

for N in range(start_block,end_block+1):
    block = node_connection.eth.get_block(N)

    # Check the transactions inside this block
    for tx_hash in block.transactions:
        purchase_details = get_purchase_details(tx_hash)

        if purchase_details is not None:
            # Get the fee for the current product
            product_name=purchase_details['product']
            fee = market_contract.functions.getFee(product_name).call(block_identifier=N)

            r_data.append({
                'Block Number': N,
                'Product Name': product_name,
                'Fee': fee
            })

    # Create a DataFrame from the transaction data
    df_r_data = pd.DataFrame([data for data in r_data])

data = {}  # Initialize a dictionary to store data

for N in range(start_block, end_block + 1):
    data[N] = {'buys': {}, 'fee': {}}

    for X in sorted(df_r_data['Product Name'].unique()):
        buys_count = df_r_data[(df_r_data['Block Number'] == N) & (df_r_data['Product Name'] == X)].shape[0]
        unique_fees = df_r_data.loc[(df_r_data['Block Number'] == N) & (df_r_data['Product Name'] == X), 'Fee'].unique()

        data[N]['buys'][X] = buys_count
        data[N]['fee'][X] = int(unique_fees)

data
# END - YOUR CODE GOES HERE


# In[16]:


"""Do not remove this cell 1."""


# In[17]:


"""Do not remove this cell 2."""


# In[18]:


"""Do not remove this cell 3."""


# ## Data for  Question 3 and 4
# 
# <font color="red">**Note: You should use the provided pre-loaded data in the variable `file_data` for Q3 to Q4.** </font>
# 
# The variable `file_data` stores the purchase details per block as per the structure defined in the previous question. You can assume that the products offered in the given data do not change across blocks.
# 

# In[19]:


"""Use the preloaded data in your working below;
This is a Read-Only cell. Remember to execute this cell once"""
with open("./a1_data.json") as f:
    file_data = json.load(f)


# ## Question 3 [1 marks]
# 
# Write a loop to complete the `demand` variable using the provided data in the `file_data` variable.
# The `demand` variable should have the following structure: 
# 
# ```python
# demand = {N: {'X': total BMM coins spent on product 'X' in the block with number N}}
# ```
# 
# The `demand` variable stores the total amount of BMM Coins spent on individual products with respect to blocks. For example, if there were `10` transactions for product `A` in block number `100`, and the fee for `A` in block `100` was `3` BMM Coins then `data[100]['A']` should store the value `30`.
# 
# <span class="label label-danger text-uppercase">Note</span>: Failure to use the provided data structure will result in **0** marks for this part.

# In[20]:


"""Predefined Variables - Do Not Change their Name;
This is a Read-Only cell. Remember to execute this cell once"""
demand = {}


# In[21]:


"""Populate the variables shown above with appropriate values here"""
# BEGIN - YOUR CODE GOES HERE

demand = {} # Initialize a dictionary to store demand

#save all block numbers in a list
N_list = []
N_list = [int(key) for key in file_data.keys()] 
#save all products in a list
X_list = []
for block_key, values in file_data.items():
    for product_name in values['fee']:
        X_list.append(product_name)
        X_list = sorted(list(set(X_list)))

for N in N_list:
    demand[N] = {}
    
    for X in X_list:
        demand_count = file_data[str(N)]['fee'][X]*file_data[str(N)]['buys'][X]
        demand[N][X] = int(demand_count)

demand
# END - YOUR CODE GOES HERE


# In[22]:


"""Do not remove this cell."""


# ## Question 4 [3 marks]
# 
# <strong> Q4 (i) [<font color="red"> 0.5 marks </font>]</strong> Plot the product fee for each product as a function of time. You can use the block number as a proxy for time units. You should use data from the `file_data` variable. Your plots should be appropriately labelled.

# In[28]:


"""Use the preloaded `file_data` from above, in your answer below"""
# BEGIN - YOUR CODE GOES HERE

columns = ['Block_Number', 'Product_Name', 'Fee', 'Buys']
df_demand = []

for block_key, values in file_data.items():
    for product_name, fee in values['fee'].items():
        fee = values['fee'][product_name]
        buys = values['buys'].get(product_name, 0)
        df_demand.append([int(block_key), product_name, fee, buys])

# Create DataFrame
df_demand = pd.DataFrame(df_demand, columns=columns)

# PLOTS 

# Set the size of the plot
plt.figure(figsize=(10, 6))

# Loop through unique product names
for X in sorted(df_demand['Product_Name'].unique()):
    df_sort = df_demand[df_demand['Product_Name'] == X]
    
    # Plot the data for each product
    plt.plot(df_sort.Block_Number, df_sort.Fee, label= "Product "+X)
    
# Set the custom tick locations
tick_interval = 15
min_block = min(df_demand['Block_Number'])
max_block = max(df_demand['Block_Number'])
custom_ticks = range(min_block, max_block + 1, tick_interval)
plt.xticks(custom_ticks)


# Set title, labels, and legend
plt.title("Product Fee For Each Product As A Function Of Time", fontweight='bold')
plt.xlabel("Block Number (Time Units)")
plt.ylabel("Product Fee")
plt.legend()

pass
# END - YOUR CODE GOES HERE


# <strong> Q4 (ii) [<font color="red"> 0.5 marks </font>]</strong> Plot the total number of units purchased for each product as a function of time. You can use the block number as a proxy for time units. You should use data from the `file_data` variable. Your plots should be appropriately labelled.

# In[29]:


"""Use the data from `file_data` variable above, in your answer below"""
# BEGIN - YOUR CODE GOES HERE

# Set the size of the plot
plt.figure(figsize=(10, 6))

# Loop through unique product names
for X in sorted(df_demand['Product_Name'].unique()):
    df_sort = df_demand[df_demand['Product_Name'] == X]
    
    # Plot the data for each product
    plt.plot(df_sort.Block_Number, df_sort.Buys, label= "Product "+X)
    
# Set the custom tick locations
tick_interval = 15
min_block = min(df_demand['Block_Number'])
max_block = max(df_demand['Block_Number'])
custom_ticks = range(min_block, max_block + 1, tick_interval)
plt.xticks(custom_ticks)

# Set title, labels, and legend
plt.title("Total Number Of Units Purchased For Products As A Function Of Time", fontweight='bold')
plt.xlabel("Block Number (Time Units)")
plt.ylabel("Total Number Of Units Purchased")
plt.legend()

# END - YOUR CODE GOES HERE


# <strong> Q4 (iii) [<font color="red"> 0.5 marks </font>]</strong> Plot the total number of currency spent on each product as a function of time. You can use the block number as a proxy for time units. You should use data from the `demand` variable. Your plots should be appropriately labelled.

# In[30]:


"""Use the data from `demand` variable above, in your answer below"""
# BEGIN - YOUR CODE GOES HERE
columns = ['Block_Number', 'Product_Name', 'Demand']
df_d = []

for N, X in demand.items():
    for product_name,fee in X.items():
        data_dict = {'Block_Number': int(N), 'Product_Name': product_name, 'Demand': fee}
        df_d.append(data_dict)
        
df_d = pd.DataFrame(df_d)

#PLOT


# Set the size of the plot
plt.figure(figsize=(10, 6))

# Loop through unique product names
for X in sorted(df_d['Product_Name'].unique()):
    df_sort = df_d[df_d['Product_Name'] == X]
    
    # Plot the data for each product
    plt.plot(df_sort.Block_Number, df_sort.Demand, label= "Product "+X)
    
    
# Set the custom tick locations
tick_interval = 15
min_block = min(df_demand['Block_Number'])
max_block = max(df_demand['Block_Number'])
custom_ticks = range(min_block, max_block + 1, tick_interval)
plt.xticks(custom_ticks)


# Set title, labels, and legend
plt.title("Total Number Of Currency Spent On Products As A Function Of Time", fontweight='bold')
plt.xlabel("Block Number (Time Units)")
plt.ylabel("Total Number Of Currency Spent")
plt.legend()
# END - YOUR CODE GOES HERE


# <strong> Q4 (iv) [<font color="red"> 1.5 marks </font>]</strong> Interpret the demands for products in the context of these two plots. Assume that these products are offered exclusively by BMM Market smart contract.

# <span class="label label-info text-uppercase">Note</span>
# <span>Write your interpretation in the Markdown cell below</span>

# The quantity demanded can be seen as the total number of units bought for products over time, and the price of a product can be equivalent to its fee. The formula for this relationship is D = Q_d * P, where D stands for demand, Q_d for the quantity demanded, and P for price.
# 
# 
# Prices for products B and C stay the same, indicating that the main determinant of demand for those goods is the quantity demanded. Due to the relatively constant price of products B and C, the demand for these goods is less volatile. The demand for product A, on the other hand, swings more because of its fluctuating price. Product A's demand movement follows the changes in its price: a value of 1 during 21188-21228, 5 during 21228-21249, and then returning to 1 during 21249-21278. The fact that the price and demand frequently match up is a noteworthy finding, pointing to a market equilibrium. Notably, product C typically has the highest demand, which is consistent with its relatively high fee. Similar to how the demand for product A does, so does that of product B.

# <font color="red">**Note: Questions 5 and 6 are independent of any previous data.** </font>
# 
# ## Question 5 [4 marks]
# 
#  This question asks you to evaluate the value of BMM Coin with respect to Australian Dollar (AUD). We will assume a simple setting where:
# - The only use of BMM Coin is to purchase products on BMM Market.
# - BMM Market sells BMM Coins in exchange for AUD at a certain exchange rate.
# - Products can be purchased only in two ways:
#   - Via an online non-crypto store (called *Classical Store*) that accepts AUD
#   - Via BMM Market that accepts BMM Coins
# - The prices of the products in AUD and BMMCoin are be subject to change.
# - The demand for products in terms of their units is fixed.
# - The seller does not care if products are purchased via BMM Coin or AUD
# 
# Transactions in the classical store can be fraudulent. If a transaction is deemed fraudulent then the store loses the fee of the product sold. The ratio of fraudulent transactions, relative demand of products are given in the table below.
# 
# | Product                 | A   | B   | C   |   |
# |-------------------------|-----|-----|-----|---|
# | Fraudulent Transactions | 2%  | 1%  | 3%  |   |
# | Demand in Units         | 60% | 30% | 10% |   |
# 
# 

# <strong> Q5 (i) [<font color="red"> 2.5 marks </font>]</strong> Complete the function, declared below, to calculate the exchange rate of BMMCoin and AUD. This function should return the amount of AUD that can be purchased with 1 BMM Coin. Clearly state any assumptions made (in the provided markdown cell).

# <span class="label label-info text-uppercase">Note</span>
# <span>Write your assumptions in the Markdown cell below</span>

# <strong> First assumption: </strong> Assuming that supply equals demand (both equal to 1), the quantity sold of each product will also equal their respective demand in units (expressed as a percentage).
# 
# <strong> Second assumption: </strong> Revenue is calculated by multiplying the quantity sold by the price, which results in the product of demand in units and price.
# 
# <strong> Third assumption: </strong> Assuming that the ratio of fraudulent transactions is fixed and the exchange rate is floating.
# 
# 
# <strong>Forth assumption:</strong> For Revenue_aud (the revenue sellers gain from selling products in AUD), the fraudulent rate is factored into the revenue formula:
# 
# (1 - fraudulent rate) * (demand * price) + fraudulent rate * 0 = (1 - fraudulent rate) * (demand * price)
# 
# 
# <strong>Fifth assumption:</strong> Assuming that the revenue sellers gain from selling products is the same regardless of whether they receive payment in BMM or AUD (since the seller does not care if products are purchased via BMM Coin or AUD), the converted revenue in BMM will be equal to the revenue in AUD:
# 
# From the question we know that: exc_rate = AUD / 1 BMM
# 
# Revenue_bmm * exc_rate = Revenue_aud => exc_rate = Revenue_aud / Revenue_bmm

# <span class="label label-info text-uppercase">Note</span>
# <span>Complete the function in the cell below</span>

# In[26]:


def bmm_aud(a_bmm, a_aud, b_bmm, b_aud, c_bmm, c_aud):
    """
    a_bmm: Price of A in bmm
    a_aud: Price of A in aud
    b_bmm: Price of B in bmm
    b_aud: Price of B in aud
    c_bmm: Price of C in bmm
    c_aud: Price of C in aud
    """
    # BEGIN - YOUR CODE GOES HERE
    
    fraud_prob = {'A': 0.02, 'B': 0.01, 'C': 0.03}
    demand = {'A': 0.60, 'B': 0.30, 'C': 0.10}
    prices_bmm = {'A': a_bmm, 'B': b_bmm, 'C': c_bmm}
    prices_aud = {'A': a_aud, 'B': b_aud, 'C': c_aud}

    Revenue_bmm = sum(demand[product] * prices_bmm[product] for product in prices_bmm)
    Revenue_aud = sum(demand[product] * (1-fraud_prob[product]) * prices_aud[product] for product in prices_aud) 
    exc_rate = Revenue_aud/Revenue_bmm
    
    return round(exc_rate,3)

bmm_aud(1,2,4,4.5,5,5.5)

    # END - YOUR CODE GOES HERE


# In[27]:


"""Do not remove this cell."""


# <strong> Q5 (ii)[<font color="red"> 0.5 marks </font>]</strong> Based on the given setting, which should be more valuable: AUD or BMM Coin? Explain why. [Word limit ≤ 50 words]

# <span class="label label-info text-uppercase">Note</span>
# <span>Write your answer in the Markdown cell below</span>

# It depends. AUD is more valuable when products' prices in AUD are less than or equal to their prices in BMM coin. Sellers are compensated through the exchange rate. However, BMM coin is more valuable when prices in AUD are higher. Sellers are compensated by setting higher prices in AUD.

# <strong> Q5 (iii) [<font color="red"> 1 marks </font>]</strong> Can there be fraudulent transactions in BMM Coin that will result in losses to BMM Market?  [Word limit < 150 words]

# <span class="label label-info text-uppercase">Note</span>
# <span>Write your answer in the Markdown cell below</span>

# Yes, there may be fraudulent BMM Coin transactions that cause the BMM Market to suffer losses. In the context of BMM Coin, fraudulent transactions may take the form of: 
# - A single entity creates numerous fake accounts in order to manipulate transactions and disrupt the credibility of the network.
# - Users generate fake transactions to manipulate the market or deceive other users.
# - Theft of BMM Coins may result from unauthorised access to accounts or smart contracts (such as through the hacking of private keys).
# 
# 
# When BMM Coin transactions are fraudulent, the revenue that sellers receive from selling BMM Coins is reduced by a factor of (1 - the fraudulent rate). This decrease in product fee revenue directly affects the BMM Market's profitability, which causes losses to the market, decreases consumer confidence in the system, and disrupts normal market operations. 
# 

# ## Question 6 [2 marks]
# 
# In this specific use case of blockchain to store product purchase information, highlight and explain one potential advantage and one potential shortcoming of the blockchain based crypto-commerce system. You should assume that a product may be offered by multiple smart contracts. [Word limit ≤ 150 words]

# <span class="label label-info text-uppercase">Note</span>
# <span>Write your answer in the Markdown cell below</span>

# <strong> Advantage: Transparency
# 
# Blockchain provides an immutable and transparent ledger. This transparency enhances trust among sellers and buyers as they can verify transactions without relying on intermediaries. Buyers can review the entire product history, including its origin, price history, and previous buyer feedback to make informed purchasing decisions. Sellers can also establish their credibility and reputation within the blockchain-based marketplace. Additionally, since a product may be offered by multiple smart contracts, blockchain ensures accurate tracking of ownership and prevents double-spending.
# 
# <strong> Disadvantage: Inconsistent Information 
#     
# However, the potential shortcoming lies in inconsistent information. Product descriptions, pricing, and transaction terms may vary between smart contracts, making it difficult for buyers to make informed purchasing decisions. Buyers may also unsure which smart contract or seller to trust, as there is no uniform information  about a specific seller or review system that covers  all instances of the product. 
