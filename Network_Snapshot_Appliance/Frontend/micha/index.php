<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="style.css" rel="stylesheet">
    <title></title>

  </head>
  <body>

<?php
    $con = new PDO('sqlite:C:\xampp\htdocs\xampp\NSA\NSA_DB.db');
?>

<?php
    $result = $myPDO->query("SELCT *FROM ip");
?>

<?php
    foreach($result as $row)
    {
        print $row['ip'] . "\n";
    }
?>
<?php
declare $MaxID INT;
declare $IP STRING;
declare $count INT;


while $count < $MaxID
  query($con,"set $IP = Select ip fron ip where id = $count;")


 ?>
<div class="links">
  <h4>Internet:(PHP) </h4>
  <h4>Doamin(php) </h4>
  <h4>Netmask(php) </h4>
</div>
<div class="vl"></div>

<div class="TableClient">
<table>
  <tr>
    <td>(php)CLIENT</td>
    <td>IP</td>
    <td>Typ</td>
    <td>OS</td>
  </tr>
</table>
</div>
<br>
<div class="TableDNS">
  <table>
    <tr>
      <td>(php)DNS</td>
    </tr>
  </table>
</div>

<div class="TableIP">
  <table>
    <tr>
      <td>(php)ip</td>
    </tr>
  </table>
</div>
<div class="ButtonScan">
<button type="button" name="ScanButton">Scan</button>
</div>
<div class="ButtonDownload">
  <button type="button" name="DownloadButton">Download</button>
</div>
  </body>
</html>
