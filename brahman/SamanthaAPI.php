<?php

include "api/samantha/controller/SamanthaCtrl.php";
include_once 'api/samantha/daos/SamanthaDao.php';
$data = file_get_contents("php://input");
$objData = json_decode($data);
$samanthaCtrl = new SamanthaCtrl();
switch ($objData->action) {
    case "converse":
        $data = $samanthaCtrl->interact($objData->question);        
        echo json_encode($data);
        break;
        
}

//$data = $samanthaCtrl->interact("#striveforgreatness");        
//        echo json_encode($data);
?>

