<?php
include "constants/AagenoConstants.php";
abstract class BasicDao{
    public $con;
    
    function __construct() {
        $this->startConnection();
    }
    
    function startConnection(){
       $this->con=mysqli_connect(AagenoConstants::$domain,  AagenoConstants::$username,  AagenoConstants::$password,  AagenoConstants::$dbname);
    }
    
    function closeConnection(){
         mysqli_close($this->con);
    }
    
        
}
?>
