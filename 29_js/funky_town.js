// Team Birdies - Shin Bamba, Johnson Li
// SoftDev1 pd8
// K28 -- Sequential Progression
// 2018-12-19T

var fibonacci = (n) => {
    console.log(fibHelp(1,0,n));
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
console.log(document);
var object = new String("yes");
var fib = document.getElementById("a");
    fib.addEventListener('click', object);
