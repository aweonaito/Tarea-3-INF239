<?php 

$html_consulta1='<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport " content="width=device-width, initial-scale=1.0">
        <title> CONSULTA 1 </title>
    </head>

    <body onload=""></body>
        <form action="" method="POST">
            <input type="text" value="{VALUE_YEAR}" placeholder="Anno" name="anno" id="consulta1_anno"><br><br>
            <input type= "submit" value="listo">
        </form>
    </body>
</html>';


$input_year=(array_key_exists('year',$_POST)) ? $_POST['year'] : "";

$html_output= str_replace("{VALUE_YEAR}", $input_year , $html_consulta1 );

echo $html_output;
if($_POST)
{
$link_consulta = "http://localhost:6969/api/consulta1/".$input_year;
$data_consulta = file_get_contents($link_consulta);
$api_output = json_decode($data_consulta, TRUE);

echo "<br><br>".$api_output;
}
?>