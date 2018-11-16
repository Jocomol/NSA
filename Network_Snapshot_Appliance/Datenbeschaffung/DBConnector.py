import sqlite3
#b = ["12.08.2018",True,"hallo.local",True]
#a = [["192.168.1.1", "client",None,None,None,None,None,None,None,None],
#     ["192.168.1.2","dhcp",None,None,"2","192.681.22.3","255.0.0.0","192.168.1.1","local",None],
#     ["192.168.1.3", "dns",None,None,None,None,None,None,None,True]]

def DBInsert(queryarray,iptable):
    conn = sqlite3.connect('/var/www/html/NSA_DB.db')
    c = conn.cursor()
    c.execute('select COUNT (*) from query')
    query_id_list = c.fetchone()
    query_id = query_id_list[0] + 1
    if queryarray[1]:
        queryarray[1] = 1
    else:
        queryarray[1] = 0
    queryarray.append(query_id)
    c.execute('insert into query (date,wanconnection, domainname, subnetmask,id) VALUES (?,?,?,?,?)', queryarray)
    for row in iptable:
        iparray = row

        c.execute('select COUNT (*) from dns')
        dns_id_list = c.fetchone()
        dns_id = dns_id_list[0] + 1

        c.execute('select COUNT (*) from dhcp')
        dhcp_id_list = c.fetchone()
        dhcp_id = dhcp_id_list[0] + 1

        dns = False
        dhcp = False
        if row[9] is not None:
            dns = True
            if row[9]:
                c.execute("insert into dns (id,working) VALUES (?,?)",(dns_id,1))
            else:
                c.execute("insert into dns (id,working) VALUES (?,?)",(dns_id,0))

        if row[5] is not None:
            dhcp = True
            c.execute("insert into dhcp (id,leastime,ip_offered,subnetmask,router,domainname) VALUES (?,?,?,?,?,?)",(dhcp_id,row[4],row[5],row[6],row[7],row[8]))

        c.execute('select COUNT (*) from ip')
        ip_id_list = c.fetchone()
        ip_id = ip_id_list[0] + 1
        rowrow = [None] * 8
        rowrow[0] = ip_id
        rowrow[1] = row[0]
        rowrow[2] = row[1]
        rowrow[3] = row[2]
        rowrow[4] = row[3]
        if dhcp:
            rowrow[5] = dhcp_id
        else:
            rowrow[5] = None
        if dns:
            rowrow[6] = dns_id
        else:
            rowrow[6] = None
        rowrow[7] = query_id

        c.execute("insert into ip (id,ip,hostname,devicetype,deviceos,dhcp_id,dns_id,query_id) VALUES (?,?,?,?,?,?,?,?)", rowrow)

        if dns:
            c.execute("insert into ip_role (ip_id,role_id) VALUES (?,?)",(ip_id,1))
        if dhcp:
            c.execute("insert into ip_role (ip_id,role_id) VALUES (?,?)",(ip_id,2))
    conn.commit()
    conn.close()


##USAGE
#DBInsert(b,a)
