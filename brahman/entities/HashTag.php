<?php
class HashTag{
    var $id;
    var $hashtag;
    var $hashtagstr;
    
    function HashTag(){
       
    } 
    
    function loadData($id1,$hashtag1){
        $this->id = $id1;
        $this->setHashTag($hashtag1);
    }
    
    function getHashTag(){
        return $this->hashtag;
    }
    
    function setHashTag($hashtag1){
        $this->hashtag = strip_tags($hashtag1);
        
        $this->hashtagstr = substr($this->hashtag, 1, strlen($this->hashtag)-1);
        
    }
    
}
?>
