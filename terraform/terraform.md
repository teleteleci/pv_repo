# Terraform


---

## Links

*   [terraform cli documentation](https://www.terraform.io/docs/commands/apply.html)
*   [azurerm configure parameters](https://www.terraform.io/docs/providers/azurerm/r/sql_database.html)
*   []

---

## File types

### template file
*   **.tf** - terraform template file

### parameter file definition

Parameters can be defined in parameters file or can be defined in ***\*.tf*** file

*   **variables.tf** - default variables file via terraform json
*   If I need other file I must use this syntax
    *   terraform apply **-var-file="*testing.tfvars*"**

###
    *   **terraform.tfvars.json** - default terraform file via json

---

## Commands
*   ***validate*** - validate only
*   ***init*** - just initialize only
*   ***plan*** - create plan
*   ***apply*** - apply plan

---

## Hints

### loop over list

```bash
resource "azurerm_sql_database" "SQL_server_databases" {
    count      = length(var.sqlServer.databases)
    depends_on = [azurerm_sql_server.sqlsrv]

    name       = "${var.sqlServer.databases[count.index]}"
```
