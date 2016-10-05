<?php
include_once 'beans/BasicBean.php';
include_once 'entites/rb.php';
include_once 'api/shabdkosh/entities/Word.php';

class WordDao extends BasicBean {
    var $starters = "अ,आ,इ,उ,ऊ,ए,ऐ,ओ,औ,क,ख,ग,घ,च,छ,ज,झ,ट,ठ,ड,ढ,त,थ,द,ध,न,प,फ,ब,भ,म,य,र,ल,व,स,श,ष,ह";
    
    var $source = "";
    
    function __construct() {
        parent::__construct();
    }
    
    function getAllWords(){
       $dbwords = R::findAll("word","id > 0 order by word_nepali asc");
       $words = array();
       foreach($dbwords as $dbWord){
           $word = new Word();
           $word->setId($dbWord->id);
           $word->setStartsWith(mb_substr(trim($dbWord->word_nepali),0,1,"utf-8"));
           $word->setEnglishWord(trim($dbWord->word_english));
           $word->setNepaliWord(trim($dbWord->word_nepali));
           array_push($words, $word);
       }
       return $words;
    }
    
    function searchWords($searchString){
       $dbwords = R::find("word","word_english = :searchString order by word_nepali asc",array(':searchString'=>$searchString));
       $words = array();
       foreach($dbwords as $dbWord){
           $word = new Word();
           $word->setId($dbWord->id);
           $word->setStartsWith(mb_substr(trim($dbWord->word_nepali),0,1,"utf-8"));
           $word->setEnglishWord(trim($dbWord->word_english));
           $word->setNepaliWord(trim($dbWord->word_nepali));
           array_push($words, $word);
       }
       return $words;
    }
    
    function getAllAlphabets(){
      return split(",", $this->starters);
    }
    
    
    
    function saveWord($wordObj){
       $word = R::dispense("word");
       $word->word_english = trim($wordObj->englishWord);
       $word->word_nepali = trim($wordObj->nepaliWord);
       R::store($word);
    }
    
    function updateWord($wordObj){
        $word = R::load('word',$wordObj->id);
        $word->word_english = $wordObj->englishWord;
        R::store($word);
    }
    
    function deleteWord($wordObj){
        $word = R::load('word',$wordObj->id);
        R::trash($word);
    }
    
    
    
    
    
    
}
?>