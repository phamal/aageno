<?php
include "/beans/NoteBean.php";
header('Content-type: application/json');
$noteBean = new NoteBean();
echo json_encode($noteBean->getNotes());
?>                