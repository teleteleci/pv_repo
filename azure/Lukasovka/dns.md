Tady je example jak pouzit DNS challenge s Azure zonou pro vygenerovani LE certifikatu:

```
az ad sp create-for-rbac --name dns-lego-contributor  --skip-assignment
az role assignment create --assignee ebda67fd-429c-4fb6-9449-921c1face9ce --role "DNS Zone Contributor" --scope /subscriptions/893ff13b-6e6b-47f5-bbb6-4b18502d99d7/resourceGroups/abx-eus-dns-rg/providers/Microsoft.Network/dnszones/velvon.com
docker run --rm -it \
-e AZURE_CLIENT_ID=ebda67fd-429c-4fb6-9449-921c1face9ce \
-e AZURE_CLIENT_SECRET=XXXX \
-e AZURE_RESOURCE_GROUP=abx-eus-dns-rg \
-e AZURE_SUBSCRIPTION_ID=893ff13b-6e6b-47f5-bbb6-4b18502d99d7 \
-e AZURE_TENANT_ID=1dbf4329-befc-4477-8668-8ec245c081bd \
-v /tmp/.lego/:/.lego/ \
goacme/lego --accept-tos --email foo@bar.com --domains sbc1.velvon.com --dns azure --dns.disable-cp --dns.resolvers 8.8.8.8 run
```
