

class Monster {
    constructor (language){
        this.language = language;
        this.stomach = [];
    }

    //stores passed argument into stomach return what has been eaten so far
    //ARRAY
    eat(food_item){
        this.stomach.push(food_item);
        return this.stomach;
    }

    //returns the passed phrase (sentence) ?
    //STRING
    speak(sentence){
        this.language = sentence;
        return this.language;
    }
}

class Gremlin extends Monster {

    //inherits how a monster eats
    eat(food_item){
        return super.eat(food_item);
    }

    //replace each word in a sentence with 'gar'
    speak(sentence){
        //string to array
        var stringArray = sentence.split(/(\s+)/);
        //filter out spaces
        var filtered = stringArray.filter(value => value !== ' '); 
        //replace each word with 'gar'
        var string = "gar ";
        if (filtered.length > 0) { 
            this.language = string.repeat(filtered.length);
            return this.language;
        }
        
    }

}

//new instance of Gremlin object to test
let gremlin = new Gremlin();

//test using the assert() method
function AssertionFailed() {
    this.message = message;
  }
  
  AssertionFailed.prototype = Object.create(Error.prototype);
  
  function assertEqual(expected, actual, message) {
    try {
      if (expected !== actual)
        throw new AssertionFailed(message);
      else
        console.log("test passed");
    } catch (e) {
      console.log("expected: '" + expected + "' does not equal actual: '" + actual + "'");
    }
  }

// test 1: language string
var gremlinSpeak = gremlin.speak("I like chicken.")
assertEqual("gar gar gar ", gremlinSpeak);


// test 2: stomach array
var gremlinEat = gremlin.eat('fish');
//console.log(gremlinEat) outputs [ 'fish' ]
assertEqual(['fish'], gremlinEat)
