$(document).ready(function(){

	$("form :input").change(function() {
		email = document.getElementById("email").value;
		pws = $('.pw');

		if (email.toLowerCase().indexOf("utoronto.ca", this.length - "utoronto.ca".length) != -1 && pws[0].value.length > 0 && pws[0].value == pws[1].value) {
			$('#createBtn').prop('disabled', false);
		} else {
			$('#createBtn').prop('disabled', true);
		}
	});	
});