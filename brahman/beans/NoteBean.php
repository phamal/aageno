<?php

include_once 'beans/BasicBean.php';
include_once 'entities/Note.php';
include_once 'entities/HashTag.php';
include_once 'daos/NoteDao.php';
include_once 'daos/HashTagDao.php';
include_once 'entites/rb.php';

class NoteBean extends BasicBean {

    var $noteDao;
    var $hashTagDao;

    function __construct() {
        parent::__construct();
        $this->noteDao = new NoteDao();
        $this->hashTagDao = new HashTagDao();
    }

    function getNotes() {
        $notes = $this->noteDao->getNotes();
        return $notes;
    }

    function addNote($noteEnt) {
        if (empty($noteEnt->id)) {
            $notedb = R::dispense('notes');
            $notedb->note = $noteEnt->note;            
            $id = R::store($notedb);
            $note = new Note();
            $note->loadData($id, $notedb->note, '', '');
            $this->tieNoteToHashTag($note);
        } else {
            $notedb = R::load("notes", $noteEnt->id);
            $notedb->note = $noteEnt->note;
            $id = R::store($notedb);
            $note = new Note();
            $note->loadData($id, $notedb->note, '', '');
            $this->tieNoteToHashTag($note);
        }
    }
    
    function tieNoteToHashTag($note){
        foreach($note->hashtags as $hashtag){
            $existinghashtag = R::findOne('hashtag', "hashtag = ?", array($hashtag->hashtag));
            $hashtagid = 0;
            if(empty($existinghashtag)){
                $hashtagdb = R::dispense('hashtag');
                $hashtagdb->hashtag = $hashtag->hashtag;
                $hastagid = R::store($hashtagdb);
            }else{
                $hashtagid = $existinghashtag->id;
            }
            $existingmap = R::findOne('hashtag_note', "hashtag_id = :tagid and note_id = :noteid", array($hashtag->hashtag));
            if(empty($existingmap)){
                $map = R::dispense('hastag_note');
                $map->hashtag_id = $hashtagid;
                $map->note_id = $note->id;
                R::store($map);
            }
            
            
        }
        
    }
    
    function deleteNote($noteid) {
        $this->noteDao->deleteNote($noteid);
    }

    function searchNoteWithHashTag($hashtag) {
        $notes = $this->noteDao->searchNoteWithHashTag($hashtag);
        return $notes;
    }

    function suggestHashTagNotes() {
        
    }

    function getHashTags() {
        return $this->hashTagDao->getAllHashTags();
    }

    function getWords(){
       echo "Getting words hai ta";
        $words = R::findAll("shabdkosh_word","id > 0");
       return $words;
    }
    
    function interact($question){
        return "Hey Prakash How are you ?";
    }
    
    function __destruct() {
        $this->noteDao->closeConnection();
    }
    

}

?>
