<?php
    
    // Database settings
    $db="architectureLycée";
    $dbhost="localhost";
    //$dbport=3306;
    $dbuser="Florian";
    $dbpasswd="hyrome";
 
    $pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
    $pdo->exec("SET CHARACTER SET utf8");
 

    $bat = $pdo->prepare("SELECT * FROM Batiment ");
    $bat->execute();
    $resultsbat =$bat->fetchALL(PDO::FETCH_ASSOC);
    $tableaubat = [];
    $tableaubat['batiments']= $resultsbat;
    $json = json_encode($tableaubat);
    echo $json;
    

?>
