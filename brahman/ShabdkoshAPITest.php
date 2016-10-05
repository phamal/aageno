<?php
include "api/shabdkosh/controller/DictCtrl.php";

$dictrl = new DictCtrl();
echo json_encode($dictrl->searchWords("egg"));

?>
