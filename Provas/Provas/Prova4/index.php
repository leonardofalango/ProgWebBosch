<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETS | Treinamentos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css.css">
    <script type="text/javascript">
      function alerta()
      {
        alert("Acabaram as vagas!");
      }
    </script>
</head>
<body>
    <nav class="navbar" id="navbar-shadow">
        <a class="nav-link" href="index.php" id="faded">
            <b>ETS | Treinamentos</b> 
        </a>
    </nav>


    <?php
      $conexao = mysqli_connect('localhost','root','');
      mysqli_select_db($conexao,'Leonardo Falango');
      $exibe="SELECT * FROM tbestudantes";
      $executa=mysqli_query($conexao,$exibe);
      
      $quant_ia = 0;
      $quant_pyhon = 0;
      $quant_robotica = 0;


      $vagas_python = 5;
      $vagas_robotica = 5;
      $vagas_ia = 5;




      while($row=mysqli_fetch_array($executa)){
          $nome= $row['nome'];
          $edv = $row['edv'];
          $curso = $row['curso'];
          $setor = $row['setor'];
          if ($curso == "Python")
            $quant_pyhon ++;
          else if ($curso == "Machine Learning")
            $quant_ia ++;
          else if ($curso == "Robótica")
            $quant_robotica ++;
      }
      
      $python = $vagas_python - $quant_pyhon; 
      $ia = $vagas_ia - $quant_ia; 
      $robotica = $vagas_robotica - $quant_robotica;
      
      if($python == 0 && $ia == 0 && $robotica == 0){
        echo "<script>alerta();</script>";
      }


    ?>



    <div class="container" style="margin-top: 30px;">
      <form action="cadastro.php" method="get">
        <div class="row">
          <div class="col-4">
            <div class="card" style="float: left;">
              <div class="card-header">
                <h2 id="cen">Programação Python</h2>
              </div>
              <div class="card-body" class="card-img">
                <img src="img/python.png" alt="Programação_Python_img" height="350px" class="card-img">
              </div>
              <div class="card-footer" style="text-align: center;">
                <button type="submit" class="btn btn-success" name="curso" value="Python" <?php if($python <= 0)echo "disabled";?>>Inscrições</button>
                <div class="alert"><h6>Vagas Disponíveis: <?php echo $python;?></h6></div>      
              </div>
            </div>
          </div>

          <div class="col-4">
            <div class="card" style="float: left;">
              <div class="card-header">
                <h2 id="cen">IA - Machine Learning</h2>
              </div>
              <div class="card-body" class="card-img">
                <img src="img/iamachinelearning.png" alt="MachineLearning_img" height="350px" class="card-img">
              </div>
              <div class="card-footer" style="text-align: center;">

                <button type="submit" class="btn btn-success" name="curso" value="Machine Learning" <?php if($ia <= 0)echo "disabled";?>>
                  Inscrições
                </button>

                <div class="alert"><h6>Vagas Disponíveis: <?php echo $ia;?></h6></div>             
              </div>
            </div>
          </div>

          <div class="col-4">
            <div class="card" style="float: left;">
              <div class="card-header">
                <h2 id="cen">Robótica</h2>
              </div>
              <div class="card-body" class="card-img">
                <img src="img/robotica_avancada.jpg" alt="Robotica_img" height="350px" class="card-img">
              </div>
              <div class="card-footer" style="text-align: center;">
                <button type="submit" class="btn btn-success" name="curso" value="Robótica" <?php if($robotica <= 0)echo "disabled";?>>Inscrições</button>
                <div class="alert"><h6>Vagas Disponíveis: <?php echo $robotica;?></h6></div>
              </div>
            </div>
          </div>
      </form>
    </div>

      
</body>
</html>