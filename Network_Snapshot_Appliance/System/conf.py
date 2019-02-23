import sqlite3


def run():
    conn = sqlite3.connect('/etc/NSA/data/NSA_DB.db')
    c = conn.cursor()
    c.execute('select COUNT (*) from configuration')
    count = c.fetchall()
    currconf = ["", "", "", "", ""]
    if int(str(count[0]).split(",")[0].strip("(")) != 0:
        c.execute('select * from configuration')
        currconf = (c.fetchone())
        print("Current configuration:")
        print("Interface:", currconf[1])
        print("DNS Repetation:", currconf[2])
        print("DHCP Repetation:", currconf[3])
        print("Cronjob Repetation:", currconf[4])
        print("--------------------------------")
        print("""Enter the following requirements,
            if you want to keep the old jsut press enter""")
    interface = input(
        "Please enter the Interface which IP should be used: ")
    dnsrepetation = input(
        """Please enter how many times the
        DNS-Discovery Script should be repeated: """)
    dhcprepetation = input("""Please enter how many times
        the DHCP-Discovery Script should be repeated: """)
    cronjob = input("""Please enter how often the scriptlib
        should be executed (cronjob) in minutes: """)
    configuration = [1, interface, dnsrepetation, dhcprepetation, cronjob]
    for i in range(len(configuration)):
        if not configuration[i]:
            configuration[i] = currconf[i]

    c.execute("delete from configuration where id = 1")
    c.execute(
        """insert into configuration (
            id,
            interface,
            dnsrepetation,
            dhcprepetation,
            cronjob)
        VALUES (?,?,?,?,?)""",
        (configuration))
    conn.commit()
    conn.close()

    if configuration[4] != currconf[4]:
        if int(configuration[4]) >= 60:
            hour = int(float(configuration[4]) / 60)
            min = int(configuration[4]) - hour * 60
            if min == 0:
                min = "*"
            hour = '*/' + str(hour)
        else:
            min = int(configuration[4])
            hour = "*"
        min = '*/' + str(min)
        cronjobstring = min + " " + hour + """ * * *   root    python3
            /etc/NSA/script/controller.py"""
        f = open("/etc/crontab", "r")
        lines = f.readlines()
        f.close()
        New = True
        f = open("/etc/crontab", 'w')
        for line in lines:
            if "NSA" not in line:
                f.write(line)
            else:
                New = False
                f.write(cronjobstring)
        if New:
            f.write(cronjobstring)
        f.write("\n")


run()
