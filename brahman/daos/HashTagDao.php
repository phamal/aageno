<?php
include_once 'BasicDao.php';
class HashTagDao extends BasicDao{
    function __construct() {
        parent::__construct();
    }
    
    function addHashTag($hashtag){
        $sql = "INSERT INTO hashtag (hashtag) VALUES ('$hashtag')";
        mysqli_query($this->con,$sql);
        if(!mysqli_query($this->con,$sql)){
            die('Error: '.  mysqli_error($this->con));
        }
        $id = mysql_insert_id();
        echo $id+"id";
        return $id;
    }
    
    function addHashtagNoteMap($hashtagid,$noteid){  
        $sql = "INSERT INTO hashtag_note (hashtag_id,note_id) VALUES ('$hashtagid','$noteid')";
        if(!mysqli_query($this->con,$sql)){
            die('Error: '.  mysqli_error($this->con));
        }
        return mysql_insert_id();
    }
    
    function getAllHashTags(){
        $result = mysqli_query($this->con,"SELECT * FROM hashtag");
        $hashtags = array();
        while($row = mysqli_fetch_array($result)) {
            $hashtag = new HashTag();
            $hashtag->loadData($row['id'],$row['hashtag']);
            array_push($hashtags, $hashtag);
        }
        return $hashtags;
    }
    
   
}
?>
