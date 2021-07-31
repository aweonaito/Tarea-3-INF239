<?php 

$html_consulta2='<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport " content="width=device-width, initial-scale=1.0">
        <title> CONSULTA 2 </title>
    </head>

    <body onload=""></body>
        <form action="" method="POST">
            <input type="text" value="{VALUE_BALANCE}" placeholder="Balance" name="balance" id="consulta2_balance"><br><br>
        </form>
    </body>
</html>';


$input_balance=(array_key_exists('balance',$_POST)) ? $_POST['balance'] : "";

$html_output= str_replace("{VALUE_BALANCE}", $input_balance, $html_consulta2);

$link_consulta2="http://localhost/api/consulta2/".$input_balance;
$data_consulta2=file_get_contents($link_consulta2);
$api_output = json_decode($data_consulta2, TRUE);

echo "<br><br>".$api_output;
?>