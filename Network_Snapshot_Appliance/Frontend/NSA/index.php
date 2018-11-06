<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="style.css" rel="stylesheet">
    <title></title>

  </head>
  <body>

<?php
    $db = new PDO('sqlite:C:\xampp\htdocs\xampp\NSA\NSA_DB.db');
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
  <td>    <?php
          $result =$db->query("SELECT count(*) FROM ip")->fetchColumn();
          echo $result;
      ?></td>

    <td>
      <?php
              $results =$db->query("SELECT ip FROM ip WHERE ID='5'")->fetchColumn();
              echo $results;
          ?>
    </td>
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
