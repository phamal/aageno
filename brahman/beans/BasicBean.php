<?php
require 'entities/rb.php';

class BasicBean{

    function __construct(){
        R::setup('mysql:host=db529950566.db.1and1.com;dbname=db529950566','dbo529950566','Machka@1');
    }
}
?>
