<?php

include_once 'beans/BasicBean.php';
include_once 'entites/rb.php';
include_once 'api/shabdkosh/daos/WordDao.php';
include_once 'api/shabdkosh/entities/Word.php';
include_once 'api/shabdkosh/entities/GroupedWords.php';

class DictCtrl {
    var $wordDao;
    
    function __construct() {
        $this->wordDao = new WordDao();
    }
    
    function getAllWords(){
        return $this->wordDao->getAllWords();
    }
    
    function searchWords($searchString){
        return $this->wordDao->searchWords($searchString);
        
    }
    
    function getGroupedWords(){
        
        
        $groupedWordsArray = array();
        $words = $this->wordDao->getAllWords();
        
        $alphabets = $this->getAllAlphabets();
        foreach($alphabets as $alphabet){
            $groupedWordsItem = new GroupedWords();
            $groupedWordsItem->startsWith = $alphabet;
            array_push($groupedWordsArray,$groupedWordsItem);
        }
        
        foreach($words as $word){
                $found = false;
                foreach($groupedWordsArray as $groupedWords){
                    
                    if( strcmp($groupedWords->startsWith,$word->getStartsWith()) == 0){
                        array_push($groupedWords->words,$word); 
                        $found = true;
                    }
                }
             
        }
        return $groupedWordsArray;
    
    }
    
    function getAllAlphabets(){
        return $this->wordDao->getAllAlphabets();
    }
    
    function saveWord($wordObj){
        if($wordObj->id){
            $this->wordDao->updateWord($wordObj);
        }else{
            $this->wordDao->saveWord($wordObj);
        }
    }
    
    function deleteWord($wordObj){
        $this->wordDao->deleteWord($wordObj);
    }
    
    function cacheDict(){
        $dictionaryJson = $this->getGroupedWords();
        //$fp = fopen('api/shabdkosh/cache/dictionary.json', 'w') or die("Unable to open file!");
        //fwrite($fp, json_encode($dictionaryJson));
        //fclose($fp);
        file_put_contents('api/shabdkosh/cache/dictionary.json', json_encode($dictionaryJson));
    }
    
    function getCacheDict(){
        $fp = fopen('api/shabdkosh/cache/dictionary.json', 'r') or die("Unable to open file!");
        return fread($fp,filesize("api/shabdkosh/cache/dictionary.json"));
        
    }
    
    
    
    
}
?>
