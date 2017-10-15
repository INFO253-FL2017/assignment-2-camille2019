var m = document.getElementById("#div");
div.innerHTML = localStorage.curLocation;

contactUs.getElementById("div").textContent = 'This is dynamically added text';
/* Run code on submit button push */
var contactUs = document.getElementById("contactUs");
contactUs.addEventListener("submit", function(event) {
	var name = contactUs.elements.namedItem("name").value;
	var subject = contactUs.elements.namedItem("subject").value;
  var message = contactUs.elements.namedItem("message").value;


	localStorage.curLocation = name + ": " + subject + ":" + message;

	var m = document.getElementById("div");
	m.innerHTML = localStorage.curLocation;
	m.classList.add("highlight");

	/* This stops the usual function of "submit" which is to send data
	to another server */
	event.preventDefault();
})
// $.ajax({url: "http://api.openweathermap.org/data/2.5/weather?lat={37.8716}&lon={122.2727}",
// 				type: "GET",
// 				dataType: "jsnop",
//
//
//
//


// def myFunction(){
//   var name = contactUS.getElementById("name").value;
//   var subject = contactUS.getElementById("subject").value;
//   var message = contactUS.getElementById("message").value;
//   var errorString = "Missing required feild(s):";
//   var errorCount = 0;
//   if (name == null){
//     errorCount+=1;
//     errorString += " name";
//   } if (subject == null){
//     errorCount+=1;
//     errorString += " subject";
//   } if (message == null){
//     errorCount+=1;
//     errorString += " message";
//   }
//   if (errorCount > 0){
//
//   }
//
//
//   }
// }
