import os
from dotenv import load_dotenv
import cbpro
load_dotenv()


auth_client = cbpro.AuthenticatedClient(os.environ['CB_KEY'], os.environ['CB_B64SECRET'], os.environ['CB_PASSPHRASE'],
                                  api_url="https://api-public.sandbox.pro.coinbase.com")
print()
def buy_order(price):
    return True