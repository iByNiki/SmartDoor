<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

body {

font-family: Arial;

}

</style>

<body>
<?php

$data = array_slice(file("distances.txt"), -1);

foreach ($data as $line) {

        if ((int) $line <= 15) {

                echo "<center><h1> Door Open </center></h1>";
        } else {

                echo "<center><h1> Door Closed </center></h1>";

        }

}

echo '<meta http-equiv="refresh" content="1">';

?>