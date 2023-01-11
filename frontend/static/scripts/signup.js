/*takes username and password and queries the api to create a new user if all conditions are met otherwise instruct user
 * on error
 */
$(document).ready(function(){

let inputs = {}
let link = "http://127.0.0.1"


  $(".submitBtn").click(function(){
	  let username = $("input[name=username]").val();
	  let password = $("input[name=password]").val();
	  let confirm_password = $("input[name=confirm_password]").val();

	  let list_inputs = [username, password, confirm_password];
	  let str_inputs = ['username', 'password', 'confirm_password'];
	  for (let i = 0; i < 3; i++){
		  if (list_inputs[i].length > 1){
			  inputs[str_inputs[i]] = list_inputs[i];
		  }
	  }
	  $.ajax({
		  dataType: "json",
		  contentType: 'application/json',
		  type: "POST",
		  headers: {
			  'Content-Type':'application/json'
		  },
		  url: link + ":5000/api/users",
		  data: JSON.stringify(inputs),
		  success: function(resp, stat){
			  window.location.replace(link + ":5001/login");
		  },
		  error: function(error, errorThrown) {
			  console.log(error)
			  console.log(errorThrown)
			  $("div[name=error]").addClass("error");
			  $("div[name=error]").html('<h4>'+error.responseJSON.error+'<h4>')
		  }
	  });
  });
	$("div[name=error]").click(function(){
		$("div[name=error]").removeClass("error");
		$("div[name=error]").html('')

	});
});
