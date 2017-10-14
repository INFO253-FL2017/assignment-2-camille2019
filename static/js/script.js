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
