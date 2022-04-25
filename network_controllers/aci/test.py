from acitoolkit.acitoolkit import *

session = Session("https://sandboxapicdc.cisco.com", "admin", "!v3G@!4@Y")
print(session)

print(session.login())
print(session.logged_in())

tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)

bds = BridgeDomain.get(session)
for bd in bds:
    print(bd.get_url(session, "tenant"))