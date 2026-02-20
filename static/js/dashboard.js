function showSection(section) {
  const title = document.getElementById("section-title");
  const content = document.getElementById("section-content");
  const container = document.getElementById("content-section");
  container.style.display = "block";

  switch (section) {
    case "attendance":
      title.innerText = "Attendance";
      content.innerText = "You have attended 18 out of 20 classes.";
      break;
    case "fees":
      title.innerText = "Fees";
      content.innerText = "Your total fees paid is Rs. 50,000. No dues.";
      break;
    case "grades":
      title.innerText = "Grades";
      content.innerText = "Your GPA is 3.8. Excellent performance!";
      break;
    case "courses":
      title.innerText = "Courses";
      content.innerText = "You are enrolled in 5 courses this semester.";
      break;
    case "percentage":
      title.innerText = "Attendance Percentage";
      content.innerText = "Your current attendance is 90%.";
      break;
    case "profile":
      title.innerText = "Profile";
      content.innerText = "Name: Ali Raza\nRoll No: 12345\nDepartment: CS";
      break;
    case "result":
      title.innerText = "Result Card";
      content.innerText =
        "Semester 1: 3.5 GPA\nSemester 2: 3.8 GPA\nSemester 3: 3.9 GPA";
      break;
    default:
      title.innerText = "";
      content.innerText = "";
  }
}
function flipCard(title, content) {
  document.getElementById("back-title").innerText = title;
  document.getElementById("back-content").innerText = content;
  document.querySelector(".flip-card").classList.add("flipped");
}

function flipBack() {
  document.querySelector(".flip-card").classList.remove("flipped");
}
