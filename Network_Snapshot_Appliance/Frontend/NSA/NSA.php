<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="style.css" rel="stylesheet">
    <title></title>

  </head>
  <body>

<?php
    $db = new PDO('/var/www/html/NSA_DB.db'); //Pfad muss noch angepasst werden wenn es auf einer Linux Syszem läuft
?>


<div class="info">
  <h4>Internet: <?php
  $internet =$db->query("SELECT wanconnection FROM query")->fetchColumn();
  echo $internet;
  ?></h4>
  <h4>Doamin: <?php
  $domain =$db->query("SELECT domainname FROM query")->fetchColumn();
  echo $domain;
  ?></h4>
  <h4>Netmask: <?php
  $netmask =$db->query("SELECT subnetmask FROM query")->fetchColumn();
  echo $netmask;
  ?></h4>
</div>
<div class="tabellen">
<div class="tablerechts">
<?php
        $sql = "SELECT * FROM ip";
      echo '
<table class="table table-bordered table-striped">
        <tr>
            <td>ID</td>
            <td>IP</td>
            <td>Hostname</td>
            <td>Devicetype</td>
            <td>DNS</td>
            <td>DHCP</td>
            <td>Query</td>
        </tr>
    </table>';
        foreach ($db->query($sql) as $row)
        {

        echo '<table class="table table-bordered table-striped">
                <tr>
                    <td>'.$row['id'].'</td>
                    <td>'.$row['ip'].'</td>
                    <td>'.$row['hostname'].'</td>
                    <td>'.$row['devicetype'].'</td>
                    <td>'.$row['dns_id'].'</td>
                    <td>'.$row['dhcp_id'].'</td>
                    <td>'.$row['query_id'].'</td>
                </tr>
            </table>';
        }
?>
<br>
<?php
        $sql = "SELECT * FROM dhcp";
      echo '
<table class="table table-bordered table-striped">
        <tr>
            <td>DHCP</td>
            <td>IP</td>
            <td>ON / OFF</td>
        </tr>
    </table>';
        foreach ($db->query($sql) as $row)
        {

        echo '<table class="table table-bordered table-striped">
                <tr>
                    <td>'.$row['id'].'</td>
                    <td>'.$row['ip_offered'].'</td>
                    <td>'.$row['router'].'</td>
                </tr>
            </table>';
        }
?>
</div>
<br>
<div id="tablelinks">
<?php
        $sql = "SELECT * FROM dns";
      echo '
<table class="table table-bordered table-striped">
        <tr>
            <td>DNS</td>
            <td>IP</td>
            <td>ON / OFF</td>
        </tr>
    </table>';
        foreach ($db->query($sql) as $row)
        {

        echo '<table class="table table-bordered table-striped">
                <tr>
                    <td>'.$row['id'].'</td>
                    <td>'.$row['working'].'</td>
                    <td>'.$row['working'].'</td>
                </tr>
            </table>';
        }
?>
</div>

</div>
<div class="ButtonScan">
<button type="button" name="ScanButton" >Scan</button>
</div>
  </body>
</html>
