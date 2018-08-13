import requests
import json

"""
The purpose of this script is to query the Walmart API and generate 1 or more response files.
"""

#----------------------------------------------------------------------------------------------------------------------
# Inputs
#----------------------------------------------------------------------------------------------------------------------

# The API key is obtained when creating a Walmart API account.
apiKey = 'API key'

# The folder in which the response files will be saved.
outputPath = 'H:\\Documents\\Data\\'

# List of base API URLs that are to be queried.
url = ['http://api.walmartlabs.com/v1/search',
       'http://api.walmartlabs.com/v1/items/46784935',
       'http://api.walmartlabs.com/v1/paginated/items', 
       'http://api.walmartlabs.com/v1/taxonomy']

# List of parameters that are to accompany each query.
parameters = [{'query':'tv', 'format':'json', 'apiKey':apiKey, 
               'sort':'bestseller', 'responseGroup':'full', 'numItems':25}, 
              {'format':'json', 'apiKey':apiKey},
              {'format':'json', 'category':'1105910', 'apiKey':apiKey},
              {'format':'json', 'apiKey':apiKey}]

# List of file names for each response.
fileName = ['search.txt', 
            'productLookup.txt', 
            'paginatedProducts.txt',
            'taxonomy.txt']


#----------------------------------------------------------------------------------------------------------------------
# Script
#----------------------------------------------------------------------------------------------------------------------
for i in range(0, 4):
    
    r = requests.get(url[i], params = parameters[i]) # send a request to the URL
    response = r.json() # retrieve the JSON response
    
    # Output the JSON response to a text file
    with open(outputPath + fileName[i], 'w', encoding='utf-8') as file:
        json.dump(response, file)
