<html>
<body>

<?php
$user = $_GET['user']
$pass = $_GET['pass']

if ($user === "admin" && $pass === "youcantguessme") {
   echo "UDCTF{d0nT_pUt_p4assw0rd3_in_th3_s0urc3}<br>";
} else {
   echo "Login failed!<br>";
}
?>

</body>
<html>