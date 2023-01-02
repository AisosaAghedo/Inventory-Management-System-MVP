$(document).ready(function(){
        let inputs = {}
        let url = "http://127.0.0.1"
	let product_sn = $(".container").attr("product_sn")

	$.ajax({
		dataType: "json",
      contentType: 'application/json',
  		type: "GET",
  		url: url + ":5000" + `/api/products/${product_sn}`,
  		success: function(res, stat){
			$("input[name=quantity]").val(res.quantity)
			$("input[name=price]").val(res.price)
		},
		error: function(err, errthrown){
			console.log(err);
			console.log(errthrown);
		}
	});



  	$("input[name=submit]").click(function(){
		inputs.quantity =  $("input[name=quantity]").val();
		inputs.price = $("input[name=price]").val();
		 $.ajax({
         		dataType: "json",
			 contentType: 'application/json',
			 data: JSON.stringify(inputs),
                	type: "PUT",
                	url: url + ":5000" + `/api/products/${product_sn}`,
                	success: function(res, stat){
				window.location.replace(url + ":5001/products")
                	},
                	error: function(err, errthrown){
                        	console.log(err);
                        	console.log(errthrown);
                	}
		 });

	});
})

