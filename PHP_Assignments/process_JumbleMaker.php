<!DOCTYPE html>
<html>
    <head>
        <title>Jumble Maker</title>
        <meta charset="utf-8">
    </head>
    <body>

        <?php 
        
            function displayError($fieldName, $errorMsg){
                global $errorCount;
                if ($errorMsg == 1){
                    echo "\"$fieldName is a required field. ";
                    ++$errorCount; 
                    $retval = ""; 
                } elseif ($errorMsg == 2){
                    echo "\"$fieldName must only contain letters. ";
                    ++$errorCount; 
                    $retval = "";
                } elseif ($errorMsg == 3){
                    echo "\"$fieldName must be between 4 and 7 characters long. ";
                    ++$errorCount; 
                    $retval = "";
                }
                
            }
            
            function validateWord($data, $fieldName){ 
                if (empty($data)) { 
                    $errorMsg = 1; 
                    displayError($fieldName, $errorMsg);
                    
                } elseif ( !preg_match ("/^[a-zA-Z\s]+$/",$data)) {
                    $errorMsg = 2;
                    displayError($fieldName, $errorMsg);
                    
                } elseif (strlen($data)<4 || strlen($data)>7){
                    $errorMsg = 3;
                    displayError($fieldName, $errorMsg);
                    
                } else {
                    $retval = strtoupper($data);
                    $retval = str_shuffle($retval);
                    return($retval);
                }
                
            }
            
            $errorCount = 0;
            $words = array();

            $words[] = validateWord($_POST['Word1'], "Word 1");
            $words[] = validateWord($_POST['Word2'], "Word 2");
            $words[] = validateWord($_POST['Word3'], "Word 3");
            $words[] = validateWord($_POST['Word4'], "Word 4");

            if ($errorCount>0){

                echo "Please use the \"Back\" button to re-enter the data.<br />\n";

            } else {

                $wordnum = 0;
                foreach ($words as $word){
                    echo "Word ".++$wordnum.": $word<br />\n";
                }
            }
        
        
        
        ?>

    </body>
</html>