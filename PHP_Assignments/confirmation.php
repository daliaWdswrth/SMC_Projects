<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cart Confirmation</title>
</head>
<body>


    
    <?php 


        
        if(!isset($_SESSION)) { 
            session_start();
            
            if ($_SESSION['oatmeal'] != 0){
                echo "Food: Oatmeal with Fruit"."<br>"."Amount: " . $_SESSION['oatmeal']."<br>";
                    
            }
            else if ($_SESSION['pancakes'] != 0){
                echo "Food: Blueberry Pancakes"."<br>"."Amount: " . $_SESSION['pancake']."<br>";
                    
            }
            else if ($_SESSION['muffin'] != 0){
                echo "Food: Banana Muffin"."<br>"."Amount: " . $_SESSION['muffin']."<br>";
                    
            }
            else if ($_SESSION['toast'] != 0){
                echo "Food: Eggs on Toast"."<br>"."Amount: " . $_SESSION['toast']."<br>";
                    
            }
            else if ($_SESSION['bagel'] != 0){
                echo "Food: Everything Bagel"."<br>"."Amount: " . $_SESSION['bagel']."<br>";
                    
            }
            else if ($_SESSION['potatoes'] != 0){
                echo "Food: Roasted Potatoes & Sausage"."<br>"."Amount: " . $_SESSION['potatoes']."<br>";
                    
            }
            
        }



        
    
    ?>

    <a href="checkout.php" >Checkout</a>
    


</body>
</html>