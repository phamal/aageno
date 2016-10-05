<?php
class Word{
    
    var $id;
    var $nepaliWord;
    var $englishWord;
    var $startsWith;
    
    function Word(){
        
    }
    
    function setNepaliWord($p_nepaliWord){
        $this->nepaliWord = $p_nepaliWord;
    }
    function getNepaliWord(){
        return $this->nepaliWord;
    }
    
    
    function setEnglishWord($p_englishWord){
        $this->englishWord = $p_englishWord;
    }
    function getEnglishWord(){
        return $this->englishWord;
    }
    
    function getStartsWith(){
        return $this->startsWith;
    }
    
    function setStartsWith($starter){
        $this->startsWith = $starter;
        
    }
    
    function setId($id){
        $this->id = $id;
    }
    function getId(){
        return $this->id;
    }
    
}
?>
