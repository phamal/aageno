
var app = angular.module('myApp', ['ngRoute','ngSanitize']);



app.config(function($routeProvider) {
    $routeProvider

    // route for the home page
    .when('/hashtags', {        
        templateUrl : '/views/hashtags.html',
        controller  : 'NoteController'
    }).when('/hashtagnotes/:hashtag', {        
        templateUrl : '/views/notes.html',
        controller  : 'HashTagNotesCtrl'
    }).when('/notes', {        
        templateUrl : '/views/notes.html',
        controller  : 'NoteController'
    }).when('/login',{
       controller   : 'LoginCtrl' 
    }).
    otherwise({
        redirectTo: '/notes'
    });			
});



app.controller('DictionaryCtrl',function($scope,$http,$routeParams) {
    $http({
            method  : 'POST',
            url     : '/NoteRestAPI.php',
            data    : {
                action : "getAllWords",
                hashtag : $routeParams.hashtag
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data)
        {
            $scope.notes = data; // response data 
        });
});

app.controller('HashTagNotesCtrl',function($scope,$http,$routeParams) {
    $http({
            method  : 'POST',
            url     : '/NoteRestAPI.php',
            data    : {
                action : "searchNoteWithHashTag",
                hashtag : $routeParams.hashtag
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data)
        {
            $scope.notes = data; // response data 
        });
});


app.controller('NoteController',  function($scope,$http) {
    $http({
        method: 'POST', 
        url: '/NoteRestAPI.php', 
        data : {
            action:"getNotes"
        }
    }).success(function(data)

    {
            $scope.notes = data; // response data 
             
        });
    $http({
        method: 'POST', 
        url: '/NoteRestAPI.php', 
        data : {
            action:"getHashTags"
        }
    }).success(function(data)

    {
            $scope.hashtags = data; // response data 
           
        });
    
    $scope.removeNote = function( note ) {
        
        $http({
            method  : 'POST',
            url     : '/NoteRestAPI.php',
            data    : {
                action : "deleteNote",
                noteId : note.id
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);

            if (data.success) {
                var index = $scope.notes.indexOf( note );
                if ( index === -1 ) {
                    return;
                }
                $scope.notes.splice( index, 1 );
            } else {
                alert("Failiure");
            }
        });
        
        
    };
    
    $scope.editNote = function( note ) {
        $scope.newnote = note;       
    };
    
    $scope.newNote = function(  ) {
        $scope.newnote = {
            note:'', 
            id:''
        };
    };
    
    $scope.addNote = function(){
        $http({
            method  : 'POST',
            url     : '/NoteRestAPI.php',
            data    : {
                action : "addNote",
                note : $scope.newnote
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data) {
            console.log(data);

            if (!data.success) {
                $http({
                    method: 'POST', 
                    url: '/NoteRestAPI.php', 
                    data : {
                        action:"getNotes"
                    }
                }).success(function(data)

                {
                        $scope.notes = data; // response data 
                    });
            } else {
                alert("Fail");
            }
        });
    };
    
    $scope.searchNoteByHashTag = function(   ) {
        if($scope.searchHashTag != 'undefined'){
            window.location.href = "#/hashtagnotes/"+$scope.searchHashTag
        }
    };
    
    
    
    $scope.getNotesByHashTag = function( tag ) {
        $http({
            method  : 'POST',
            url     : '/NoteRestAPI.php',
            data    : {
                action : "searchNoteWithHashTag",
                hashtag : tag
            },  // pass in data as strings
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded'
            }  // set the headers so angular passing info as form data (not request payload)
        })
        .success(function(data)
        {
            $scope.notes = data; // response data 
        });
    };
    
   

});

app.controller('SummernoteController', ['$scope', '$attrs', function($scope, $attrs) {
    'use strict';

    var currentElement,
        summernoteConfig = $scope.summernoteConfig || {};

    if (angular.isDefined($attrs.height)) { summernoteConfig.height = $attrs.height; }
    if (angular.isDefined($attrs.focus)) { summernoteConfig.focus = true; }
    if (angular.isDefined($attrs.lang)) {
      if (!angular.isDefined($.summernote.lang[$attrs.lang])) {
        throw new Error('"' + $attrs.lang + '" lang file must be exist.');
      }
      summernoteConfig.lang = $attrs.lang;
    }

    summernoteConfig.oninit = $scope.init;
    summernoteConfig.onenter = function(evt) { $scope.enter({evt:evt}); };
    summernoteConfig.onfocus = function(evt) { $scope.focus({evt:evt}); };
    summernoteConfig.onblur = function(evt) { $scope.blur({evt:evt}); };
    summernoteConfig.onpaste = function(evt) { $scope.paste({evt:evt}); };
    summernoteConfig.onkeydown = function(evt) { $scope.keydown({evt:evt}); };
    if (angular.isDefined($attrs.onImageUpload)) {
      summernoteConfig.onImageUpload = function(files, editor, welEditable) {
        $scope.imageUpload({files:files, editor:editor, welEditable:welEditable});
      };
    }

    this.activate = function(scope, element, ngModel) {
      var updateNgModel = function() {
        var newValue = element.code();
        if (ngModel && ngModel.$viewValue !== newValue) {
          ngModel.$setViewValue(newValue);
          if ($scope.$$phase !== '$apply' || $scope.$$phase !== '$digest' ) {
            scope.$apply();
          }
        }
      };

      summernoteConfig.onkeyup = function(evt) {
        updateNgModel();
        $scope.keyup({evt:evt});
      };

      element.summernote(summernoteConfig);

      var editor$ = element.next('.note-editor'),
          unwatchNgModel;
      editor$.find('.note-toolbar').click(function() {
        updateNgModel();

        // sync ngModel in codeview mode
        if (editor$.hasClass('codeview')) {
          editor$.on('keyup', updateNgModel);
          if (ngModel) {
            unwatchNgModel = scope.$watch(function () {
              return ngModel.$modelValue;
            }, function(newValue, oldValue) {
              editor$.find('.note-codable').val(newValue);
            });
          }
        } else {
          editor$.off('keyup', updateNgModel);
          if (angular.isFunction(unwatchNgModel)) {
            unwatchNgModel();
          }
        }
      });

      if (ngModel) {
        ngModel.$render = function() {
          element.code(ngModel.$viewValue || '');
        };
      }

      currentElement = element;
    };

    $scope.$on('$destroy', function () {
      currentElement.destroy();
    });
  }])
  .directive('summernote', [function() {
    'use strict';

    return {
      restrict: 'EA',
      transclude: true,
      replace: true,
      require: ['summernote', '^?ngModel'],
      controller: 'SummernoteController',
      scope: {
        summernoteConfig: '=config',
        init: '&onInit',
        enter: '&onEnter',
        focus: '&onFocus',
        blur: '&onBlur',
        paste: '&onPaste',
        keyup: '&onKeyup',
        keydown: '&onKeydown',
        imageUpload: '&onImageUpload'
      },
      template: '<div class="summernote"></div>',
      link: function(scope, element, attrs, ctrls) {
        var summernoteController = ctrls[0],
            ngModel = ctrls[1];

        summernoteController.activate(scope, element, ngModel);
      }
    };
  }]);


app.controller('OptCtrl', function($scope) {
                $scope.options = {
                    height: 150,
                    toolbar: [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['fontsize', ['fontsize']],
                        ['color', ['color']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['height', ['height']]
                    ]
                };
            })
            .controller('CodeCtrl', function($scope) {
                $scope.text = "Hello World";
            })
            .controller('CallbacksCtrl', function($scope) {
                $scope.init = function() { console.log('Summernote is launched'); }
                $scope.enter = function() { console.log('Enter/Return key pressed'); }
                $scope.focus = function(e) { console.log('Editable area is focused'); }
                $scope.blur = function(e) { console.log('Editable area loses focus'); }
                $scope.paste = function() { console.log('Called event paste'); }
                $scope.keyup = function(e) { console.log('Key is released:', e.keyCode); }
                $scope.keydown = function(e) { console.log('Key is pressed:', e.keyCode); }
            });


app.controller('LoginCtrl', function($scope) {
        $scope.loginAction = function(   ) {
            alert("Doing the login action");
        
    };
    
});

