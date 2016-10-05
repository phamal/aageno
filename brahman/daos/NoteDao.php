<?php
include_once 'BasicDao.php';
class NoteDao extends BasicDao{
    function __construct() {
        parent::__construct();
    }
    
    function addNote($note){
        $sql = "INSERT INTO notes (note) VALUES ('$note->note')";
        mysqli_query($this->con,$sql);
        $id = mysql_insert_id($this->con);
        return $id;
    }
    
    function updateNote($note){
        $sql = "update notes set note = '$note->note' where id = '$note->id'";
        if(!mysqli_query($this->con,$sql)){
            die('Error: '.  mysqli_error($this->con));
        }
        
    }
    
    function getNotes(){       
        $result = mysqli_query($this->con,"SELECT * FROM notes order by cdate desc");
        $notes = array();
        while($row = mysqli_fetch_array($result)) {
            $note = new Note();
            $note->loadData($row['id'],$row['note'],$row['cdate'],$row['title']);
            array_push($notes, $note);
        }
        return $notes;
    }
    
    function deleteNote($noteid){
        $sql = "delete from notes where id = '$noteid'";
        if(!mysqli_query($this->con,$sql)){
            die('Error: '.  mysqli_error($this->con));
        }
    }
    
    function searchNoteWithHashTag($hashtag){
        if(substr($hashtag,0, 1) != '#'){
            $hashtag = "#".$hashtag;
        }
        $result = mysqli_query($this->con,"SELECT * FROM notes where note like '%$hashtag%' order by cdate desc ");
        $notes = array();
        while($row = mysqli_fetch_array($result)) {
            $note = new Note();
            $note->loadData($row['id'],$row['note'],$row['cdate']);
            array_push($notes, $note);
        }
        return $notes;
    }
}
?>
