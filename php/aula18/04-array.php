<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../_css/estilo.css"/>
  <meta charset="UTF-8"/>
  <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
  <pre>
    <?php
      $c = array(3=>5,
                 1=>9,
                 0=>8,
                 7=>7);
      $c[] = "E";
      unset($c[0]);
      print_r($c);
    ?>
  </pre>
</div>
</body>
</html>