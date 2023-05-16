<!DOCTYPE html>
<html>
    <head>
        <title>Register Form</title>
        <meta charset="utf-8">
    </head>
    <body>

        <?php

            if (empty ($_POST['name']) || empty ($_POST['age']) || empty ($_POST['average']))
                echo "<p>You must enter your name, age, and average.
                Click your browser's Back button to return to the Register Page.</p>\n";

            else {
                $registerForm = fopen("registerform.txt", "ab");
                $name = addslashes($_POST['name']);
                $age = $_POST['age'];
                $average = $_POST['average'];

                if (is_numeric($age) && is_numeric($average)){

                    if (is_writeable("registerform.txt")) {
                        if (fwrite($registerForm, $name .", " . $age . ", " . $average . "\n"))
                            echo "<p>Thank you for registering!</p>\n";
                        else
                            echo "<p>Cannot add your details to the form.</p>";
                    } else 
                            echo "<p>Cannot write to the file .</p >\n";
                        fclose($registerForm) ;

                } else {
                    echo "<p>You must enter a valid number for age & average.</p>\n";
                }
                
            }
                
                

        ?>



    </body>
</html>