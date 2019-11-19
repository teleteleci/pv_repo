Kdyby nekdo potreboval rychle rozjet docker stroj v azure a nechtel delat ARM sablonu, nebo se otravovat s extension setem a scriptovanim, kvuli instalanci dockeru, tak lze pouzit neco jako: ( posilal jsem to ted uhlikovi, kvuli pozadavkum pro android emulator )




Tohle funguje docela spolehlive a je to jednoduchy, muzes to pouzit i ty ... Nebo to doporucit lidem/vyvojarum. Proste to vezme image z azure a nainstaluje to na nej posledni verzi dockeru ( samozrejmne to podporuje postcommandy a vic jinych argumentu )

docker-machine create \
--driver azure \
--azure-subscription-id $subscriptionID \
--azure-image Canonical:UbuntuServer:18.04-LTS:latest \
--azure-no-public-ip \
--azure-resource-group $rg \
--azure-size Standard_D8s_v3 \
--azure-ssh-user sysadmin \
--azure-subnet $subnet \
--azure-vnet $vnet \
foobar



[11:41 AM] Lukas Mrtvy
    Kdyby nekdo potreboval rychle rozjet docker stroj v azure a nechtel delat ARM sablonu, nebo se otravovat s extension setem a scriptovanim, kvuli instalanci dockeru, tak lze pouzit neco jako: ( posilal jsem to ted uhlikovi, kvuli pozadavkum pro android emulator )




Tohle funguje docela spolehlive a je to jednoduchy, muzes to pouzit i ty ... Nebo to doporucit lidem/vyvojarum. Proste to vezme image z azure a nainstaluje to na nej posledni verzi dockeru ( samozrejmne to podporuje postcommandy a vic jinych argumentu )

docker-machine create \
--driver azure \
--azure-subscription-id $subscriptionID \
--azure-image Canonical:UbuntuServer:18.04-LTS:latest \
--azure-no-public-ip \
--azure-resource-group $rg \
--azure-size Standard_D8s_v3 \
--azure-ssh-user sysadmin \
--azure-subnet $subnet \
--azure-vnet $vnet \
foobar


Kdyz by si to mel delat vyvojar sam, tak mu muzes pridat neco jako:

az role assignment create \
    --assignee $id \
    --role Contributor \
    --scope /subscriptions/$subscriptionID/resourceGroups/$rg

Tady je jeste potreba mit pravo na propojeni/cteni do vnetu a subnetu.
A kdyz to umisti do te resource grupy ze scopu, tak se mu vytvori stroj a credentials bude mit u sebe na lokalu

Bude to dobre fungovat pro lidi, kteri si ten stroj budou spravovat sami a vy tim usetrite cas...

(1 liked)​[11:49 AM] Lukas Mrtvy
    A treba takhle:

--azure-custom-data=/spust/muj/container/nebo/cokoliv/jineho

tam muzou vecpat neco, co by se melo udelat pri vytvoreni.
