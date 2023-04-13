<?php
    
    // Database settings
    $db="architectureLycée";
    $dbhost="localhost";
    //$dbport=3306;
    $dbuser="Florian";
    $dbpasswd="hyrome";
 
    $pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
    $pdo->exec("SET CHARACTER SET utf8");
 
    #$choixBatiment = $_GET["NomBatiment"];
    #echo $choixBatiment ;
    $eta = $pdo->prepare("SELECT NumEtage FROM Etage NATURAL JOIN Batiment WHERE NomBatiment = ? ");
    $eta->execute([$_GET["NomBatiment"]]);
    $resultsEta =$eta->fetchALL(PDO::FETCH_ASSOC);
    $tableauEta = [];
    $tableauEta['etages']= $resultsEta;
    $json = json_encode($tableauEta);
    echo $json;

?>