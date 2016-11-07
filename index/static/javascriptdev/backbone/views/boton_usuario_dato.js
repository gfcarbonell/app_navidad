var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class BotonUsuarioDato extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#boton_usuario_dato_template").html());
		this.render();
	}
	events()
	{
		return { 
				"click #boton_usuario_dato"  			  : "open_close_configuracion",
			   };
	}
	open_close_configuracion(e)
	{
		e.preventDefault();
		$("#usuario_panel_configuracion").toggle(300);
	}
    render() 
	{
        this.$el.html(this.template());
		return this;
    }

}

module.exports = BotonUsuarioDato;
