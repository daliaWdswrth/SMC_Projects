

let num = 6

//This function handles the recursion and string copying
function Recurse(str, n) {
    if (n < 0) {
        return "";
      }
    if (n === 1) {
        return str + str;
      }
    else {
        result = str + Recurse(str, n - 1); 
        return result;
      }
      
}

//This function formats output (result) of Recurse function and determines whether it is odd or even
function RecursiveCopy(str, n){

  result = Recurse(str, n);

  if (n % 2 == 0){
    console.log(result, "has an odd number of blue's");
  }
  else {
    console.log(result, "has an even number of blue's");
  }

}

//call function, print output
RecursiveCopy("blue", num)
