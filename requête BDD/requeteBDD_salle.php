<?php
    
    // Database settings
    $db="architectureLycée";
    $dbhost="localhost";
    //$dbport=3306;
    $dbuser="Florian";
    $dbpasswd="hyrome";
 
    $pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
    $pdo->exec("SET CHARACTER SET utf8");
 
   
    $sal = $pdo->prepare("SELECT NumSalle FROM Salle NATURAL JOIN Etage WHERE NumEtage = ? ");
    $sal->execute([$_GET["NumEtage"]]);
    $resultsSal =$sal->fetchALL(PDO::FETCH_ASSOC);
    $tableauSal = [];
    $tableauSal['salles']= $resultsSal;
    $json = json_encode($tableauSal);
    echo $json;

?>