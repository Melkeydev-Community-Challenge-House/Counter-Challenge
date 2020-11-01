fun main(args: Array<String>) {
    println("Would you like to start counting?[y/n]")
    var answer: Char = try{readLine()!!.toLowerCase()!![0]} catch(e: Exception) {'e'}
    println(">>$answer\n")
    
    while(answer != 'y' && answer != 'n'){
        println("...")
        answer = try{readLine()!!.toLowerCase()!![0]} catch(e: Exception) {'e'}
        println(">>$answer\n")
    }
    
    if (answer == 'n'){
        println("Too bad, see ya")
        System.exit(1)
    }
    
    println("Up to what would you like to count?")
    var top = try {readLine()!!.toInt()} catch(e: Exception) {-1}
    println(">>$top\n")
    
    while(top < 0){
        println("I need a natural number greater than zero pls")
        top = try {readLine()!!.toInt()} catch(e: Exception) {-1}
        println(">>$top\n")
    }
    
    if(top == 0){
        println("You could've just said No")
        System.exit(1)
    }
    
    println("Ok, let's count up to $top, press ENTER to advance")
    var num = 0
    var input: String? = "nothing"
    
    while(num < top){
        input = readLine()
        println(">>$input\n")
        if(input.isNullOrEmpty()){
            num = num.inc()
            println("We're at $num out of $top")
        }
        else{
            println("Try again")
        }
    }
    println("Done!")
}
