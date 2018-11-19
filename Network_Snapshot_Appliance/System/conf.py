import sqlite3

def run():
    conn = sqlite3.connect('/etc/NSA/data/NSA_DB.db')
    c = conn.cursor()
    c.execute('select COUNT (*) from query')
    count = c.fetchone()
    print (count)
    if count[0] != 0:
        c.execute('select * from configuration')
        currconf = (c.fetchone())
        print ("Current configuration:")
        print ("Interface:",currconf[1])
        print ("DNS Repetation:", currconf[2])
        print ("DHCP Repetation:", currconf[3])
        print ("Cronjob Repetation:", currconf[4])
        print ("--------------------------------")
    print ("Enter the following requirements, if you want to keep the old jsut press enter")
    interface = input("Please enter the Interface which IP should be used: ")
    dnsrepetation = input("Please enter how many times the DNS-Discovery Script should be repeated: ")
    dhcprepetation = input("Please enter how many times the DHCP-Discovery Script should be repeated: ")
    cronjob = input("Please enter how often the scriptlib should be executed (cronjob) in minutes: ")
    configuration = [1,interface,dnsrepetation,dhcprepetation,cronjob]

    for i in range(len(configuration)):
        if configuration[i] == "":
            configuration[i] = currconf[i]

    c.execute("delete from configuration where id = 1")
    c.execute("insert into configuration (id,interface,dnsrepetation,dhcprepetation,cronjob) VALUES (?,?,?,?,?)",(configuration))
    conn.commit()
    conn.close()



'''
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#

    #setup cronjob
'''
run()
