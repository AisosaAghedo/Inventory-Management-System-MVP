$(document).ready(function(){
	let url = "http://127.0.0.1:"
	$(".delete").click(function(){
		let product_sn = $(this).parent(".project-box").attr("product_sn")

		 $.ajax({
		dataType: "json",
      contentType: 'application/json',
  		type: "DELETE",
  		url: url + "5000" + `/api/products/${product_sn}`,
  		success: function(response, stat){
			location.reload(true)
		},
		error: function(error, errorthrown){
			console.log(error);
			console.log(errorthrown);
		}
		 })


	})

})
