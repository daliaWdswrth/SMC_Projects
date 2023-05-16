<!DOCTYPE html>
<html>
    <head>
        <title>Show Guest Book</title>
        <meta charset="utf-8">
    </head>
    <body>

        <pre>
            <?php

                $myfile = @readfile("guestbook.txt");
                if (!$myfile) 
                {
                    echo "File could not be opened";
                }

                

            ?>
        </pre>
        



    </body>
</html>