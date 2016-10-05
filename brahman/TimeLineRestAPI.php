<?php
include "../beans/TimeLineBean.php";
$timeLineBean = new TimeLineBean();
var_dump($timeLineBean->getEvents());
?>