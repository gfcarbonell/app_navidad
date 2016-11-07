var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class BotonCloseMenu extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#boton_close_menu_template").html());
		this.render();
	}
	events()
	{
		return { 
				"click #boton_close_menu"  			  : "close_menu",
			   };
	}
	close_menu(e)
	{
		e.preventDefault();
		$("#aside_menu_modulo").hide(300);
	}
    render() 
	{
        this.$el.html(this.template());
		return this;
    }

}

module.exports = BotonCloseMenu;
