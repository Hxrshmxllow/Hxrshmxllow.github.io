var totalGPA = 0;
var points = 0;
var prevGPA = 0;
var prevPoints = 0;
function add(){

    var level = parseFloat(document.getElementById("level").value);
    var grade = parseFloat(document.getElementById("grade").value);
    var credits = parseFloat(document.getElementById("credits").value);
    
    
    var gpa = level + grade;
    totalGPA += (level + grade) * credits;
    points += credits; 
    prevPoints = credits;
    prevGPA = (level + grade) * credits;
    var finalGPA = (totalGPA / points).toFixed(3);
    document.getElementById("finalGPA").innerHTML = "GPA: " + finalGPA;
    
}

