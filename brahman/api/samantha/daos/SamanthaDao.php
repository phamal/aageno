<?php
include_once 'beans/BasicBean.php';
include_once 'entites/rb.php';
include_once 'api/samantha/entities/Note.php';

class SamanthaDao extends BasicBean {
    
    function __construct() {
        parent::__construct();
    }
    
    function getTodos(){
        return "Clean house, Clean car";
    }
    
    function getNotes($hashtag){
        $notes = R::findAll("notes","note like '%$hashtag%' order by cdate desc");
        $returnNotes = array();
        if($notes){
            foreach($notes as $note){
                $returnNote = new Note();
                $returnNote->loadData($note->id, $note->note, $note->cdate, $note->title);                
                array_push($returnNotes, $returnNote);
            }
        }
        return $returnNotes;
    }
    
    function getHashTags(){
        $dbhashtags = R::findAll("hashtag");
        $hashtags = array();
        foreach($dbhashtags as $dbhashtag){
            array_push($hashtags,"#".$dbhashtag->hashtag);
        }
        return $hashtags;
    }
    
    function getHashTagsString(){
        $hashtags = $this->getHashTags();
        return implode(", ", $hashtags);
    }
    
    function saveNote($note){
        $notedb = R::dispense('notes');
        $notedb->note = $note;            
        return R::store($notedb);
    }
}