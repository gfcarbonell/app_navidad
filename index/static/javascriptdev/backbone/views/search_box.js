var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
var csrf = require("../csrf");
Backbone.$ = $;


class SearchBox extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#input_search_registro_template").html());
		this.render();
	}

	events()
	{
		return {
				"keyup #input_search_registro"					  : "search",
				"keypress #input_search_registro"				  : "search_enter",
				"submit #form_search_input"						  : "enviar",
			   };
	}

	search_enter(e)
	{
		if(e.key=="Enter")
		{
			console.log(e.key );
			this.enviar(e);
		}

	}

	search(e)
	{
		e.preventDefault();
		this.enviar(e);
	}

	enviar(e)
	{
		e.preventDefault();
		$.ajax({
					url : $("#form_search_input").attr("action"),

					type: $("#form_search_input").attr("method"),

					dataType: "text",

					data: {"search_registro":$("#input_search_registro").val(),},

					async: true,

					success: function(data){
						//$("#container_table_body").html(data);
						//$("#form_search_input").submit();
						//return true;
						$("#container_table_body").replaceWith($('#container_table_body', $(data)));

					},

					error: function (data, textStatus, jqXHR) {
		                var errors = $.parseJSON(data.responseText);
		                console.log(xhr.status + ": " + xhr.responseText);
				    }

				});
		return false;
	}

  render()
	{
			this.$el.html(this.template());
		 	return this;
  }

}

module.exports = SearchBox;
