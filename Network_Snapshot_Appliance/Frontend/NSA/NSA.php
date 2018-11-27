<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="style.css" rel="stylesheet">
    <title></title>

  </head>
  <body>

<?php
    $db = new PDO('sqlite:C:\xampp\htdocs\xampp\NSA\NSA_DB.db'); //Pfad muss noch angepasst werden wenn es auf einer Linux Syszem läuft
?>


<div class="info">
  <h4>Internet: <?php
  if ($internet = "0")
  $intstatus = "OFF";
  else
  $intstatus = "ON";
  $internet =$db->query("SELECT wanconnection FROM query")->fetchColumn();
  echo $intstatus;
  ?></h4>
  <h4>Doamin: <?php
  $domain =$db->query("SELECT domainname FROM query")->fetchColumn();
  echo $domain;
  ?></h4>
  <h4>Netmask: <?php
  $netmask =$db->query("SELECT subnetmask FROM dhcp")->fetchColumn();
  echo $netmask;
  ?></h4>
  <h4>Datum: <?php
  $netmask =$db->query("SELECT date FROM query")->fetchColumn();
  echo $netmask;
  ?></h4>
</div>
<div class="tabellen">
<div class="tablerechts">
<?php
$query = $_POST['query'] ?? 'john doe';;
        $sql = "SELECT * FROM ip WHERE query_id LIKE '$query'";
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
</div>
<br>
<div class="tablelinks">
  <?php
          $sql = "SELECT dhcp.id, dhcp.ip_offered, ip.id FROM dhcp INNER JOIN ip ON dhcp.id = ip.id WHERE query_id LIKE '$query'";
        echo '
  <table class="table table-bordered table-striped">
          <tr>
              <td>DHCP</td>
              <td>IP</td>
          </tr>
      </table>';
          foreach ($db->query($sql) as $row)
          {
          echo '<table class="table table-bordered table-striped">
                  <tr>
                      <td>'.$row['id'].'</td>
                      <td>'.$row['ip_offered'].'</td>
                  </tr>
              </table>';
          }
  ?>
  <br>
<?php
$query = $_POST['query'] ?? 'john doe';;
        $sql = "SELECT dns.id, dns.working, ip.query_id, ip.dns_id, ip.ip   FROM dns INNER JOIN ip ON dns.id = ip.dns_id WHERE query_id LIKE '$query'";
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
          $working = $row['working'];
          if ($working = "0")
          $status = "OFF";
          else
          $status = "ON";
          if($working ="1")
          $farbe = "green";
          else
          $farbe ="red";


        echo '<table class="table table-bordered table-striped">
                <tr>
                    <td>'.$row['id'].'</td>
                    <td>'.$row['ip'].'</td>
                    <td style = background-color:'.$farbe.' >'.$status.'</td>
                </tr>
            </table>';
        }
?><br>
<form action="" method="post">
Query: <input type="text" name="query" />
<input type="Submit" value="Absenden" />
</form>
</div>
  </body>
</html>
