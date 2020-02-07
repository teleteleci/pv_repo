# Configure the Microsoft Azure Provider
provider "azurerm" {
    version = "=1.36.0"
}

# Resource group
resource "azurerm_resource_group" "resourceGroup" {
    name = "${var.environmentShort}-${var.rg.domain}-rg"
    location = "West Europe"

    tags = {
        subscription = "${var.environment.subscription}"
        note = "Delete anytime"
    }
}

# resource "azurerm_sql_database" "example" {
#     name = "${var.environmentShort}-${var.sqlServer.domain}-sqlsrv"
#     resource_group_name =
#     location                         = "${azurerm_resource_group.example.location}"
#     server_name                      = "${azurerm_sql_server.example.name}"
#     edition                          = "Basic"
#     collation                        = "SQL_Latin1_General_CP1_CI_AS"
#     create_mode                      = "Default"
#     requested_service_objective_name = "Basic"
# }
#
# resource "azurerm_sql_firewall_rule" "example" {
#   name                = "allow-azure-services"
#   resource_group_name = "${azurerm_resource_group.example.name}"
#   server_name         = "${azurerm_sql_server.example.name}"
#   start_ip_address    = "0.0.0.0"
#   end_ip_address      = "0.0.0.0"
# }
