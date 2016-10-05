
var app = angular.module('dict', ['ngRoute','ui.bootstrap','ngSanitize']);



app.config(function($routeProvider) {
    $routeProvider

    // route for the home page
    .when('/index',{
        templateUrl : '/views/shabdkosh/main.html',
        controller  : 'NavController'
    })
    .when('/browse', {  
        templateUrl : '/views/shabdkosh/browse.html',
        controller  : 'DictionaryController'
    })
    .when('/admin',{
        templateUrl : '/views/shabdkosh/admin.html',
        controller : 'DictionaryController'
    }) 
    .when('/update',{
        templateUrl : '/views/shabdkosh/update.html',
        controller : 'UpdateController'
    }). 
    otherwise({
        redirectTo: '/browse'
    });			
});

app.directive('onEnter', function() {
    return {
        scope: {onEnter: '&'},
        link: function(scope, element) {
            console.log(scope);
            element.bind("keydown keypress", function(event) {
                if(event.which === 13) {
                    scope.onEnter();
                    scope.$apply();
                }
            });
        }
    }
});





app.controller('DictionaryController',function($scope,$http,$routeParams) {
    $http({
        method  : 'POST',
        url     : '/ShabdkoshAPI.php',
        data    : {
            action : "getGroupedWords"
        },  // pass in data as strings
        headers : {
            'Content-Type': 'application/x-www-form-urlencoded'
        }  // set the headers so angular passing info as form data (not request payload)
    })
    .success(function(data)
    {
        $scope.groupedWordsList = data; // response data 
        $scope.name = "Prakash Hamal";
           
    })
    .error(function(){
        alert("some problem");
    });
    
    
    $http({
        method  : 'POST',
        url     : '/ShabdkoshAPI.php',
        data    : {
            action : "getAllAlphabets"
        },  // pass in data as strings
        headers : {
            'Content-Type': 'application/x-www-form-urlencoded'
        }  // set the headers so angular passing info as form data (not request payload)
    })
    .success(function(data)
    {
        $scope.alphabets = data; // response data 
           
    })
    .error(function(){
        alert("some problem");
    });
    
   
});



app.controller('NavController',function($scope,$http,$routeParams) {
    $scope.searchWord = function(){
        $http({
            method  : 'POST',
            url     : '/ShabdkoshAPI.php',
            data    : {
                action : "searchWords",
                searchString : $scope.searchString
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            $scope.words = data;  
            console.log(data);
            window.location.href = "#/index"
        }).error(function(data){
            console.log(data);
        })
        ;
    };
});

app.controller('UpdateController',function($scope,$http,$routeParams) {
  
    $http({
        method  : 'POST',
        url     : '/ShabdkoshAPI.php',
        data    : {
            action : "getAllWords"
        },  // pass in data as strings
        headers : {
            'Content-Type': 'application/x-www-form-urlencoded'
        }  // set the headers so angular passing info as form data (not request payload)
    })
    .success(function(data) {
        $scope.words = data; 
        console.log(data);
    });
        
    $scope.saveWord = function(pword){
        console.log(pword);
        
        $http({
            method  : 'POST',
            url     : '/ShabdkoshAPI.php',
            data    : {
                action : "saveWord",
                word : pword
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);
        });
        
        
    };
    
    $scope.deleteWord = function(pword){
        
        $http({
            method  : 'POST',
            url     : '/ShabdkoshAPI.php',
            data    : {
                action : "deleteWord",
                word : pword
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);
            var index = $scope.words.indexOf(pword);
            if (index > -1) {
                $scope.words.splice(index, 1);
            }
        });
    }
  
});

app.controller('AdminController',function($scope,$http,$routeParams) {
    $http({
        method  : 'POST',
        url     : '/ShabdkoshAPI.php',
        data    : {
            action : "getAllWords"
        },  // pass in data as strings
        headers : {
            'Content-Type': 'application/x-www-form-urlencoded'
        }  // set the headers so angular passing info as form data (not request payload)
    })
    .success(function(data)
    {
        $scope.words = data; // response data 
        $scope.name = "Prakash Hamal";
        console.log(data);
           
    })
    .error(function(){
        alert("some problem");
    });
    
    $scope.readSource = function(   ) {        
        if($scope.source != 'undefined'){
            var words = $scope.source.split(" ");
            $scope.newwords = [];
            for(var i in words){
                var word_exist = false;
                for(var k in $scope.words){
                    if($scope.words[k].nepaliWord == words[i]){
                        word_exist = true;
                    }
                }
                $scope.newwords.push({
                    "nepaliWord":words[i],
                    "englishWord":$scope.words[k].englishWord,
                    "wordExist":word_exist
                });
                
            }
        }
    };
    $scope.saveWord = function(pword){
        $http({
            method  : 'POST',
            url     : '/ShabdkoshAPI.php',
            data    : {
                action : "saveWord",
                word : pword
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);
        });
    };
    $scope.resetCache = function(pword){
        $http({
            method  : 'POST',
            url     : '/ShabdkoshAPI.php',
            data    : {
                action : "resetCache"
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);
            alert(data.msg);
        });
    };
});

app.controller('AccordionDemoCtrl', function ($scope) {
    $scope.oneAtATime = true;

    $scope.groups = [
    {
        title: 'Dynamic Group Header - 1',
        content: 'Dynamic Group Body - 1'
    },
    {
        title: 'Dynamic Group Header - 2',
        content: 'Dynamic Group Body - 2'
    }
    ];

    $scope.items = ['Item 1', 'Item 2', 'Item 3'];

    $scope.addItem = function() {
        var newItemNo = $scope.items.length + 1;
        $scope.items.push('Item ' + newItemNo);
    };

    $scope.status = {
        isFirstOpen: true,
        isFirstDisabled: false
    };
});
