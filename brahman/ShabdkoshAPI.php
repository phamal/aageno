<?php

include "api/shabdkosh/controller/DictCtrl.php";


$data = file_get_contents("php://input");

$objData = json_decode($data);
$dictrl = new DictCtrl();

//echo $dictrl->getCacheDict();

switch ($objData->action) {
    case "getAllWords":
        echo json_encode($dictrl->getAllWords());
        break;
     case "getGroupedWords":
        //echo json_encode($dictrl->getGroupedWords());
         echo $dictrl->getCacheDict();
         break;
    case "getAllAlphabets":
        echo json_encode($dictrl->getAllAlphabets());
        break;
    case "saveWord":
        $dictrl->saveWord($objData->word);
        $data = array("msg" => "Successfully added the word" );
        echo json_encode($data);
        break;
    case "deleteWord":
        $dictrl->deleteWord($objData->word);
        $data = array("msg" => "Successfully added the word" );
        echo json_encode($data);
        break;
    case "searchWords":
        echo json_encode($dictrl->searchWords($objData->searchString));
        break;
    case "resetCache":
        $dictrl->cacheDict();
        $data = array("msg" => "Successfully reset cache" );
        echo json_encode($data);
        break;
    default :
        //echo json_encode($dictrl->getWords());
        echo $objData->action;
        break;
}
?>
