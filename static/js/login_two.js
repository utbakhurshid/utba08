// student/main.js
function studentLogin(event) {
  event.preventDefault();

  
  const rollno = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Dummy credentials check
  if (
    username === "ahmed" &&
    password === "ali123"
  ) {
    window.location.href = "/dashboard"; // redirect to student dashboard
  } else {
    alert("Invalid student credentials.");
  }
}
