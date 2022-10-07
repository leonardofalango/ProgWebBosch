
<!-- -=--=--=--=--=--=--=--=--=--=--=--=--=--=- PAGINA USADA COMPLETAMENTE PARA ENVIAR DADOS PARA O BANCO DE DADOS -=--=--=--=--=--=--=--=--=--=--=--=--=--=--->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecionando...</title>
    <meta http-equiv="refresh" content="0.000001; index.php">
</head>
<body>
</body>
</html>

<!-- PODERIAMOS CRIAR UMA TABLE PARA CADA CURSO, PARA QUE O NÚMERO DE VAGAS, A CARGA HORARIA ENTRE OUTROS FOSSEM DEFINIDOS PELO BANCO DE DADOS.-->

<?php
    $curso = $_POST['curso'];
    $setor = $_POST['setor'];
    $edv = $_POST['edv'];
    $nome = $_POST['nome'];


    $conexao = mysqli_connect('localhost','root','');
    mysqli_select_db($conexao,'Leonardo Falango');
    $grava= "INSERT INTO `tbestudantes` (`curso`,`setor`,`edv`,`nome`) VALUES ('$curso','$setor','$edv','$nome');";
    $executa=mysqli_query($conexao,$grava) or die ("Não foi possível executar.");
?>