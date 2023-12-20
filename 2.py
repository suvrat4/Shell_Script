from msrestazure.azure_active_directory import AADTokenCredentials
from azure.mgmt.compute import ComputeManagementClient
import webbrowser

# Replace these with your Azure details
subscription_id = '<SubscriptionId>'
resource_group_name = '<ResourceGroupName>'
bastion_name = '<BastionName>'
username = '<YourUsername>'
password = '<YourPassword>'

# Set up Azure credentials
credentials = AADTokenCredentials(
    resource='https://management.azure.com/',
    tenant_id='<YourTenantId>',
    client_id='<YourClientId>',
    client_secret='<YourClientSecret>'
)

# Set up Compute Management Client
compute_client = ComputeManagementClient(credentials, subscription_id)

# Get Azure Bastion details
bastion = compute_client.bastion_hosts.get(resource_group_name, bastion_name)

# Construct the Bastion URL
bastion_url = f'https://{bastion.fqdn}'

# Open the Bastion URL in the default web browser
webbrowser.open(bastion_url)

# Note: Handling MFA (e.g., using an authenticator app) manually is required.
