import sqlite3

def run():

    interface = input("Please enter the Interface which IP should be used: ")
    dnsrepetation = input("Please enter how many times the DNS-Discovery Script should be repeated: ")
    dhcprepetation = input("Please enter how many times the DHCP-Discovery Script should be repeated: ")
    configuration = [1,interface,dnsrepetation,dhcprepetation]
    conn = sqlite3.connect('/var/www/html/NSA_DB.db')
    c = conn.cursor()
    c.execute("delete from configuration where id = 1")
    c.execute("insert into configuration (id,interface,dnsrepetation,dhcprepetation) VALUES (?,?,?,?)",(configuration))
    conn.commit()
    conn.close()

    #setup cronjob
run()
