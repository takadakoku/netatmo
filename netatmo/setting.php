<?php

$rain_limit = $_POST["rain"];
if(is_numeric($rain_limit)){  
  $fp = fopen("rain.conf", "a");
  ftruncate($fp, 0);
  fwrite($fp, $rain_limit);
  fclose($fp);
 }


$filename = "rain.conf";
$rain = fopen($filename, "r");

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
 <form action="" method="POST">
   <h1>設定雨量は<?=fgets($rain);?>mmです。</h1> 
    <input type="text" name="rain" placeholder="">
    <input type="submit" name="submit" value="sent"> 
    <button><a href="stop_rain_down.php">リセット</a></button> 
 </form> 
</body>
</html>
