<?php
header('Content-Type: text/html; charset=utf-8');
if (isset($_POST['source'])) {
    $source = $_POST['source'];
    $words = explode(" ", $source);
}
?>
<html>
    <head>
        <script src="/resources/jquery/jquery-2.1.1.min.js" type="text/javascript"></script>
        <script type="text/javascript">
            function acceptWord(elem){
                var word_nepali = elem.parent().find(".word_nepali").val();
                var word_english = elem.parent().find(".word_english").val();
                $.ajax({
                    type: "POST",
                    url: "/ShabdkoshAPI.php",
                    data: { nepaliWord: word_nepali, englishWord: word_english,action:"saveWord" },
                    headers : {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    } 
                })
                .done(function( msg ) {
                    alert( "Data Saved: " + msg );
                });
                
            }
            
            function denyWord(elem){
                var word = elem.parent().find(".word").val();
                alert("Lets deny this one "+word);
            }
        </script>    
        <style type="text/css">
            .words{

            } 
            .wordedit{
                border:1px solid #cdcdcd;
                padding: 5px;
                margin-top: 5px;
            }
        </style>    
    </head>
    <body>
        <form name="readSource" action="parser.php" method="post">
            <textarea  rows="10" cols="50" name="source" >
            </textarea>
            <br />
            <input type="Submit" value="Read source" />
            <br />
            <br />
        </form>

        <div class="words">
            <?php foreach ($words as $word): ?>
                <div class="wordedit">
                    <input type="text" class="word_nepali" value="<?php echo $word; ?>" />
                    <input type="text" class="word_english" value="" />
                    <input type="button" onClick="acceptWord($(this))" value="Good">&nbsp;
                    <input type="button" onClick="denyWord($(this))" value="Not good"><br />
                </div>
            <?php endforeach; ?>
        </div>    
    </body>
</html>