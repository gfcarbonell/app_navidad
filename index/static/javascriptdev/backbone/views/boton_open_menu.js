var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class BotonOpenMenu extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#boton_open_menu_template").html());
		this.render();
	}
	events()
	{
		return { 
				"click #boton_open_menu"  			  : "open_menu",
			   };
	}
	open_menu(e)
	{
		e.preventDefault();
		$("#aside_menu_modulo").show(300);
	}
    render() 
	{
        this.$el.html(this.template());
		return this;
    }

}

module.exports = BotonOpenMenu;
