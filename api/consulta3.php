<?php 

$html_consulta3='<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport " content="width=device-width, initial-scale=1.0">
        <title> CONSULTA 3 </title>
    </head>

    <body onload=""></body>
        <form action="" method="POST">
            <input type="text" value="{VALUE_PAIS}" placeholder="Pais" name="pais" id="consulta3_pais"><br><br>
        </form>
    </body>
</html>';

$input_pais=(array_key_exists('pais',$_POST)) ? $_POST['pais'] : "";

$html_output= str_replace("{VALUE_PAIS}", $input_pais,$html_consulta3);

$link_consulta3="http://localhost/api/consulta3/".$input_pais;
$data_consulta3=file_get_contents($link_consulta3);
$api_output = json_decode($data_consulta3, TRUE);

echo "<br><br>".$api_output;
?>