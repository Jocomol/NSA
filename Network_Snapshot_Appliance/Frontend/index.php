<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="style.css" rel="stylesheet">
    <title></title>
  </head>
  <body>
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

    <?php
    declare @IP text;
    declare @Typ text;
    declare @os Text;
    declare @IDs INT;

     for each ^ID^ in ^Table^ set @IP = IP where ID ?>

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
