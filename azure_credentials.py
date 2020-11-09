import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# We don't need to specify any credentials here, because Stratosphere will take
# care of injecting them.
CREDS = DefaultAzureCredential()

# The `azure-resource-name` is generated by the Stratosphere and will be returned
# when creating your resource. It is the same resource name as for the postgresql
# resource
client = SecretClient(vault_url="https://oxykil88mluhdd0o678krkc9.vault.azure.net", credential=CREDS)

secret_key = "administrator-login-password"
secret = client.get_secret(secret_key)


os.environ["PSQL_USERNAME"] = secret.name
os.environ["PSQL_PASSWORD"] = secret.value

import psycopg2

# The Azure resource name is generated by the Stratosphere.
azure_resource_name = "oxykil88mluhdd0o678krkc9"

# Update connection string information
host = f"{azure_resource_name}.postgres.database.azure.com"
db_name = "postgres"
username = f"stratosphere@{azure_resource_name}"
sslmode = "require"

# Construct connection string, we use the password we retrieved from the Key Vault above.
conn_string = f"host={host} user={username} dbname={db_name} password={password} sslmode={sslmode}"
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Verify we can connect
cursor.execute("SELECT 1;")

# Cleanup
conn.commit()
cursor.close()
conn.close()