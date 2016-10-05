<?php

include_once 'beans/BasicBean.php';
include_once 'entites/rb.php';
include_once 'api/samantha/daos/SamanthaDao.php';

class SamanthaCtrl {

    var $samanthaDao;

    function __construct() {
        $this->samanthaDao = new SamanthaDao();
    }

    function interact($question) {
        $hashtag = $this->getHashTag($question);
        if(strpos($question, '@savenote') !== false) {
            $question = str_replace("@savenote", "", $question);
            return $this->createNote($this->samanthaDao->saveNote($question));
        }else if (strpos($question, 'hey') !== false) {
            return $this->createNote('Hey :)');
        }if (strpos($question, 'haha') !== false) {
            return $this->createNote('Hahaha whats so funny :)');
        } else if (strpos($question, 'k cha') !== false) {
            return $this->createNote('Thik cha. Ani timro ni ?');
        } else if (strpos($question, 'commands') !== false) {
            return $this->createNote('You can do several commands to me like : >>remindme() >>savenote() >>todo etc. And I will perform the task for you ');
        } else if (strpos($question, 'actions') !== false) {
            return $this->createNote('You can ask me to perform these things : >>remindme() >>savenote() >>todo etc.');
        } else if (strlen($hashtag) > 0) {
            return $this->samanthaDao->getNotes($hashtag);
        } else if (strpos($question, 'hashtags') !== false) {
            return $this->createNote($this->samanthaDao->getHashTagsString());
            
        } else if (strpos($question, 'help') !== false) {
            return $this->createNote('You do actions >>savenote("What a wonderful day today.") '
                    . '>>todo("Library book renew due on 02/28/2015"). '
                    . ' you can search notes by hashtags eg. #todo #striveforgreatness.'
                    . ' If you are searching for notes write more to see more of the notes.');
        }

        return $this->createNote("You must be confused. You can ask for help. And we can have more fun conversation !! :)");
    }
    
    function createNote($ntStr){
        $notes = array();
        $note = new Note();
        $note->note = $ntStr;
        array_push($notes, $note);
        return $notes;
    }

    function getHashTag($input) {
        $words = split(' ', $input);
        if ($words) {
            foreach ($words as $word) {
                if (substr($word, 0, 1) == '#') {
                    return substr($word, 1, strlen($word));
                }
            }
        }
        return "";
    }

}

?>
