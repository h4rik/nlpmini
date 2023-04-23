function submitGoals() {
	const checkboxes = document.querySelectorAll('input[type="checkbox"]');
	let selectedGoals = [];

	checkboxes.forEach(function(checkbox) {
		if (checkbox.checked) {
			selectedGoals.push(checkbox.value);
		}
	});

	if (selectedGoals.length === 0) {
		document.getElementById("result").innerHTML = "Please select at least one goal.";
	} else {
		document.getElementById("result").innerHTML = "You have selected the following goals: " + selectedGoals.join(", ");
	}
}