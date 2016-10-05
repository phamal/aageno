<?php
class Note{
    var $id;
    var $note;
    var $cdate;
    var $title;
    var $hashtags;
    var $notesummary;
    var $commaSeperatedHastags;
    var $noteHtmlEscape;
    
    function Note(){
       $this->hashtags = array();
       //$this->hashtags = array("apple","banana");
    } 
    
    function setNote($notestr){
        $this->note = $notestr;
       // $this->getHashTags();
    }
    
    
    function loadData($id,$note,$cdate,$title){
        $this->id = $id;
        $this->note = $note;
        $this->cdate = $cdate;
        
        $this->loadHashTags();
        $this->loadTitle();
        $this->loadNoteSummary();
        $this->escapeNote();
        
    }
    
    function loadTitle(){
        $this->title = substr(strip_tags($this->note),0,50);
    }
    
    function loadNoteSummary(){
        $this->notesummary =substr(strip_tags($this->note),0,100);
    }
    
    function escapeNote(){
        
    }
    
    function getNotes(){
        
    }
    
    function setId($id){
        $this->id = $id;
    }
    
    function getId(){
        return $this->id;
    }
    
    function loadHashTags(){
        if(empty($this->hashtags)){
            $words = split(' ', $this->note);
            $first = true;
            if($words){
                foreach($words as $word){
                    if(substr($word, 0,1) == '#'){
                        $hashTag = new HashTag();
                        $hashTag->loadData(1,  substr($word, 1,strlen($word)));
                        array_push($this->hashtags,$hashTag);
                        $this->commaSeperatedHastags .= (($first)?'':',').substr($word,1,  strlen($word));
                        $first = false;
                    }                
                }
            }
        }
        return $this->hashtags;
    }
    
    
}
?>
