var fibonacci = (n) => {
    return fibHelp(1, 0, n);
};

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
