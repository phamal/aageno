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
   
    
    
    function loadData($id,$note,$cdate,$title){
        $this->id = $id;
        $this->note = $note;
        $this->cdate = $cdate;
        $this->title = $title;
    }
    
    
    
}
?>
