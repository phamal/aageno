
var app = angular.module('myApp', ['ngRoute','ngSanitize']);





app.controller('SamanthaController',  function($scope,$http) {
 
    $scope.converse = function(  ) {
        
        $http({
            method  : 'POST',
            url     : '/SamanthaAPI.php',
            data    : {
                action : "converse",
                question:$scope.question
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);
            $scope.notes = data;
            $scope.recentQuestion = $scope.question;
            $scope.question = "";  
        });
        
        
    };
    
    $scope.editNote = function( note ) {
        $scope.newnote = note;       
    };
    
    
   

});