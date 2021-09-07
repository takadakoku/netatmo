<?php

$num = $_POST["rain"];
if(is_numeric($num)){  
  $fp = fopen("rain.conf", "a");
  ftruncate($fp, 0);
  fwrite($fp, $num);
  fclose($fp);
}else{
  echo "<h1>エラーです。</h1>";
}

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
    <input type="text" name="rain" placeholder="">
    <input type="submit" name="submit" value="sent">  
</body>
</html>
