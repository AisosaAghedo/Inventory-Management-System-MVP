
$(document).ready(function(){
	let inputs = {}
	let user_id = $("header").attr("user_id");
	let url = "http://127.0.0.1"


  $("input[name=submit]").click(function(){
	  let name = $("input[name=name]").val();
	  let serial_number = $("input[name=serial_number]").val();
	  let category = $("input[name=category]").val();
	  let expiry_date = $("input[name=expiry_date]").val();
	  let quantity = $("input[name=quantity]").val();
	  let price = $("input[name=price]").val();
	  let input_list = [name, serial_number, category, expiry_date, quantity, price];
	  let input_str = ['name', 'serial_number', 'category', 'expiry_date', 'quantity', 'price'];

    	for (let i = 0; i < input_list.length; i++){
      	if (input_list[i].length > 0){
        	inputs[input_str[i]] = input_list[i];
      	}
    	}

    	$.ajax({
	    	dataType: "json",
	    	type: "POST",
	    	headers: {
		    	'Content-Type':'application/json'
	    	},

	    	url: url + `:5000/api/users/${user_id}/products`,
	    	data: JSON.stringify(inputs),
	    	success: function(resp, stat){
		    window.location.replace(url + ":5001/products");
      },
      		error: function(error, errorThrown) {
			console.log(error);
			console.log(errorThrown)


       		}
  

		});
});
})
