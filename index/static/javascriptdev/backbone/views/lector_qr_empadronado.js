var $ 			  = require('jquery');
var _         = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;

class LectorQREmpadronado extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#lector_codigo_barra_qr_template").html());
		this.render();
		this.leer_codigo_barra_qr();
	}

  leer_codigo_barra_qr(e)
  {

  }

  render()
	{
			this.$el.html(this.template());
		 	return this;
  }

}

module.exports = LectorQREmpadronado;
