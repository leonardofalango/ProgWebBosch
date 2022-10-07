<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETS | Cadastro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css.css">
    <script type="text/javascript">
      function alerta()
      {
        alert("Curso inválido. Redirecionando para a Página Principal");
        window.location="index.php";
      }
    </script>
</head>
<body>

  <!-- -=--=--=--=--=--=- PREVININDO SAFADENHOS DE ALTERAREM O VALOR DO CURSO NO LINK DA PÁGINA -=--=--=--=--=--=- -->
  <?php $curso = $_GET["curso"];?>
  <?php if ($curso != "Machine Learning" && $curso != "Python" && $curso != "Robótica") echo "<script>alerta()</script>"?>
  <?php
   $conexao = mysqli_connect('localhost','root','');
    mysqli_select_db($conexao,'Leonardo Falango');
    $exibe="SELECT * FROM tbestudantes";
    $executa=mysqli_query($conexao,$exibe);

    $vagas_python = 5;
    $vagas_robotica = 5;
    $vagas_ia = 5;

    while($row=mysqli_fetch_array($executa)){
        $nome= $row['nome'];
        $edv = $row['edv'];
        $cursobanco = $row['curso'];
        $setor = $row['setor'];
        if ($cursobanco == "Python")
          $vagas_python --;
        else if ($cursobanco == "Machine Learning")
          $vagas_ia --;
        else if ($cursobanco == "Robótica")
          $vagas_robotica --;
    }
    if($vagas_robotica == 0 && $curso == "Robótica")
      echo "<script>alerta()</script>";
    if($vagas_python == 0 && $curso == "Python")
      echo "<script>alerta()</script>";
    if($vagas_ia == 0 && $curso == "Machine Learning")
      echo "<script>alerta()</script>";
    ?>

    <nav class="navbar" id="navbar-shadow">
        <a class="nav-link" href="index.php" id="faded">
            <b>ETS | Treinamentos</b> 
        </a>
    </nav>

    <div class="container">
        <form action="form.php" method="post" class="was-validated">
          <div class="form-group" style="margin-top: 80px;">
            <label for="nome">Nome:</label>
            <input type="name" class="form-control" id="nome" aria-describedby="emailHelp" placeholder="Nome Completo" name="nome" required>
          </div>
    
          <div class="form-group">
            <label for="EDV">EDV:</label>
            <input type="number" class="form-control" id="EDV" placeholder="EDV" name="edv" required>
          </div>
    
          <div class="form-group">
            <label for="setor">Setor:</label>
            <input type="text" class="form-control" name="setor" required>
          </div>

          <div class="form-group">
            <label for="curso">Curso:</label>
            <!-- <div class="alert col-12 bg-light">
                Curso
            </div> -->
            <select name="curso" class="col-12" style="padding: 10px" id="readonly" aria-disabled="true">
              <option value="<?php echo $curso?>"><?php echo $curso?></option>
            </select>
          </div>


          <div class="form-group col-12" style="margin-top: 30px">
            <button type="submit" class="btn btn-dark col-12" name='Cadastrar' value="1">Cadastrar</button>
          </div>
        </form>
      </div>

</body>