var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class PanelMenuUsuario extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#panel_menu_template").html());
		this.render();
	}

	events()
	{
		return {
				"click #menu_personales" 		  : "show_personales",
				"click #menu_domicilio" 		  : "show_domicilio",
				"click #menu_extras" 		      : "show_extras",
			   };
	}

	show_personales(e)
	{
		e.preventDefault();
		$("#panel_personales").show();
		$("#menu_personales").addClass("color-black").parent().addClass("background-white");

		$("#panel_domicilio").hide();
		$("#menu_domicilio").removeClass("color-black").parent().removeClass("background-white");

		$("#panel_extras").hide();
		$("#menu_extras").removeClass("color-black").parent().removeClass("background-white");

	}

	show_domicilio(e)
	{
		e.preventDefault();
		$("#panel_domicilio").show();
		$("#menu_domicilio").addClass("color-black").parent().addClass("background-white");;

		$("#panel_personales").hide();
		$("#menu_personales").removeClass("color-black").parent().removeClass("background-white");

		$("#panel_extras").hide();
		$("#menu_extras").removeClass("color-black").parent().removeClass("background-white");

	}


	show_extras(e)
	{
		e.preventDefault();
		$("#panel_extras").show();
		$("#menu_extras").addClass("color-black").parent().addClass("background-white");;

		$("#panel_personales").hide();
		$("#menu_personales").removeClass("color-black").parent().removeClass("background-white");

		$("#panel_domicilio").hide();
		$("#menu_domicilio").removeClass("color-black").parent().removeClass("background-white");

	}

    render()
	{
        this.$el.html(this.template());
		return this;
    }

}

module.exports = PanelMenuUsuario;
