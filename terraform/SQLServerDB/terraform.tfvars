environment = {
    subscription = "ABX_DEV"
    envPrefix = "abdedv"
}

rg = {
    domain = "pvtest"
    location = "West Europe"
    tags = {
        subscription = "xxx"
        note = "Delete anytime"
    }
}

sqlServer = {
    administrator_login = "unoadmin"
    version = "12.0"
    aad_admin = {
        role_name = "DEV_ADMINS"
        azure_aad_object_id = "be66ed76-1d61-43d4-873e-322a29ada4db"
        tenant_id = "1dbf4329-befc-4477-8668-8ec245c081bd"
    }
    databases = [
        {
            db_name = "db1"
            db_size = "104857600"
            sku_name = "S0"
            tier = "Standard"
        },
        {
            db_name = "db2"
            db_size = "104857600"
            sku_name = "S0"
            tier = "Standard"
        }
    ]
    virtualNetworkRules = {
        firewallRules = [
            {
                name = "Prague-vpn",
                startIpAddress = "40.118.94.225"
                endIpAddress = "40.118.94.225"
            },
            {
                name = "Prague-vlan"
                startIpAddress = "80.188.193.178"
                endIpAddress = "80.188.193.178"
            }
        ]
        virtualNetworkList = [
            {
                vnetName = "abdedv-dev-vnet",
                subnetName = "abdedv-dev-tools-subnet"
                subnetId = "/subscriptions/a0dcddb9-cf21-4f85-b8d7-d3bdf0cb0426/resourceGroups/abdedv-network-rg/providers/Microsoft.Network/virtualNetworks/abdedv-dev-vnet/subnets/abdedv-dev-tools-subnet"
            }
        ]
    }
}
