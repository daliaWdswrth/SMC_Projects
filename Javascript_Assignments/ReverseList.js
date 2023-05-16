
//define list
let list = {
    value: "first",
    next:{
        value: "second",
        next:{
            value: "third",
            next: null
        }
    }
}

//convert list to array
function listToArray (list){
    var listArray = [];
    for (var node = list; node; node = node.next){
        listArray.push(node.value);
    }
    return listArray;
}
//reverse array
function reverseArray (arr){
	var reverseArray = [];
    var listLength = arr.length; 
    for(var i = 0; i < listLength; i++){
  	    reverseArray.push(arr.pop());
    }
    return reverseArray;
}
//convert array to list
function arrayToList (arr){
    for ( var i = arr.length - 1; i >=0; i--){
        var list = { value: arr[i], next:{...list}};
    }
    return list;
}
//call functions
arrayOfList = listToArray(list);
reverseOfArray = reverseArray(arrayOfList)
//print final result (reversed list)
console.log(arrayToList(reverseOfArray)) 
