var h = document.getElementById("h");
var thelist = document.getElementById("thelist");
var b = document.getElementById("b");
var fb = document.getElementById("fb");
var fibList = document.getElementById("fiblist");

var fibonacci = (n) => {
    return fibHelp(1, 0, n);
}

// Helper for fibonacci
var fibHelp = (startNum, sumSoFar, numTimes) => {
    if (numTimes == 0){
        return sumSoFar;
    }
    return fibHelp(startNum + sumSoFar, startNum, numTimes - 1);
}

thelist.addEventListener("mouseover", (e) => {
    // console.log(e);
    // console.log("mousing over ol");
    h.innerHTML = e.target.innerHTML;
});

thelist.addEventListener("mouseout", () => {
    h.innerHTML = "Hello World!";
});

thelist.addEventListener("click", (e) => {
    e.target.remove();
});

b.addEventListener("click", () => {
    var newItem = document.createElement("li");
    newItem.innerHTML = "WORD";
    thelist.appendChild(newItem);
});

var counter = 0;
fb.addEventListener("click", () => {
    var numToAdd = document.createElement("li");
    numToAdd.innerHTML = fibonacci(counter);
    fibList.appendChild(numToAdd);
    counter++;
})
