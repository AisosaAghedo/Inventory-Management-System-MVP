$(document).ready(function(){
  let url = "http://127.0.0.1:"
  let input = {};

  $(".search-input").change(function(){
    let search = $("input.search-input").val();
    if (search.length < 1){
      return;
    }

    input.query = search;
    checked = search;
    $.ajax({
		dataType: "json",
      contentType: 'application/json',
  		type: "POST",
  		url: url + "5000" + "/api/product_search",
  		data: JSON.stringify(input),
  		success: function(response, stat){

        if ($("div[name=filter]").html().length > 0)
        {
          $("div[name=filter]").html('')
        }
        for (let res of response){
          $("div[name=filter]").append(`
	  <div class="project-box-content-header">
        <div class="project-box">
                <p class="box-content-header">${res.name}</p>
                <p class="box-content-subheader">${res.category}</p>
                <p class="box-content-subheader">${res.quantity}</p>
      </div>
      </div>`);
        }

        },
      error: function(error, errorThrown) {
            console.log(error);
            console.log(errorThrown);
       }
    });
});

});
