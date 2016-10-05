<?php
include_once 'beans/BasicBean.php';
include_once 'entites/rb.php';

class DictionaryCtrl extends BasicBean {
    
    function __construct() {
        parent::__construct();
       
    }
    
    function getWords(){
       echo "Getting words hai ta";
       $words = R::findAll("shabdkosh_word","id > 0");
       return $words;
    }
    
    
    
    
}?>
