<?php 
  
include "beans/NoteBean.php";
  
  
        
    
  
  $noteBean = new NoteBean();
  $note = new Note();
  $note->note = "Nikita is very pretty #pretty #nikita";
  $noteBean->addNote($note);
  
  /*
  echo "Testing getting all notes:<br />";
  $allNotes = $noteBean->getNotes();
  echo "Notes Count : "+sizeof($allNotes)."<br />";
  
  echo "Testing hashtags of the notes<br />";
  foreach($allNotes as $note){
      $count = sizeof($note->hashtags);
      echo $count."<br />";
      echo $note->commaSeperatedHastags;
      if($count > 0){
          var_dump($note->hashtags);
          
      }
      
  }
  
  echo "Testing creation of note:<br />";
  $note = new Note();
  $note->loadData("", "nikita is pretty", "", "nikita");
  $noteid = $noteBean->addNote($note);
  echo "------Adding note success !!-- and the new id is '$noteid'<br />";
  
  echo "Testing search of note:<br />";
  $notes = $noteBean->searchNoteWithHashTag("nikita");
  echo sizeof($notes);
  echo "------Adding note success !!<br />";
   * /
   */
  /*
  echo "Testing -- Getting hashtags";
  $hashtags = $noteBean->getHashTags();
  echo sizeof($hashtags);
  echo "------Adding note success !!<br />";
*/
  //TODO once the test suite is complete need to destroy the data.
  
  
?> 