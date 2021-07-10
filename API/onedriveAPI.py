from microsoftgraph.client import Client
client = Client('CLIENT_ID', 'CLIENT_SECRET', account_type='by defect common', office365=True)




# token = client.exchange_code(redirect_uri, code)

# token = client.set_token(token)

# root_items = client.drive_root_items()

print(client.client_id())

#help(Client)