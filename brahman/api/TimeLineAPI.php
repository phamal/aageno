<?php
include "../beans/TimeLineBean.php";
$data = file_get_contents("php://input");
$objData = json_decode($data);
$noteBean = new NoteBean();
$noteBean->addNote($objData->note);
?>
