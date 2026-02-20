// student/main.js
function studentLogin(event) {
  event.preventDefault();

  const batch = document.getElementById("batch").value;
  const degree = document.getElementById("degree").value;
  const rollno = document.getElementById("rollno").value;
 

  // Dummy credentials check
  if (
    batch === "2023" &&
    degree.toUpperCase() === "ICS" &&
    rollno.toUpperCase() === "ICS-101" 
    
  ) {
    window.location.href = "/login_two"; // redirect to student dashboard
  } else {
    alert("Invalid student credentials.");
  }
}
