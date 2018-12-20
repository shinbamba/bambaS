// Team ShinZ (Shin Bamba, Thomas Zhao)
// SoftDev1 pd8
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-19

/////////////////////////////// WRAPPER FUNCTIONS ///////////////////////////////
var fibonacci_wrap = () => {
    console.log(fibonacci(5))
    p_tag.innerHTML = "fibonacci(5): " + fibonacci(5);
};

var gcd_wrap = () => {
    console.log(gcd(45, 12))
    p_tag.innerHTML = "gcd(45, 12): " + gcd(45, 12);
};

var randomStudent_wrap = () => {
    console.log(randomStudent())
    p_tag.innerHTML = "randomStudent(): " + randomStudent();
};

/////////////////////////////// ACTUAL FUNCTIONS ///////////////////////////////
var fibonacci = (n) => {
    return fibHelp(1, 0, n);
};

// Helper for fibonacci
var fibHelp = (startNum, sumSoFar, numTimes) => {
    if (numTimes == 0){
        return sumSoFar;
    }
    return fibHelp(startNum + sumSoFar, startNum, numTimes - 1);
};

var gcd = (a, b) => {
    if(b == 0){
        return a;
    }
    return gcd(b, a % b);
};

var students = ["Bob", "Tim", "Kevin", "John", "Sally"];
var randomStudent = () => {
    var randomIndex = Math.floor(Math.random() * students.length);
    return students[randomIndex];
};

//////////////////////////////// GETTING ELEMENT IDS //////////////////////////////
var fib = document.getElementById("a");
var greatest = document.getElementById("b");
var student = document.getElementById("c");

////////////////////////////// ADDING EVENT LISTENERS /////////////////////////////
fib.addEventListener('click', fibonacci_wrap);
greatest.addEventListener('click', gcd_wrap);
student.addEventListener('click', randomStudent_wrap);

//////////////////////////////// DISPLAYING RESULTS //////////////////////////////
var p_tag = document.getElementById("results");