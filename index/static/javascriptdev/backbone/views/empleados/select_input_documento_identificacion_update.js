var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;
var DocumentosIdentificaciones = require("../../collections/documentos_identificaciones");


class SelectInputDocumentoIdentificacionUpdate extends Backbone.View
{

	initialize(x)
	{
		this.documentos_identificaciones = new DocumentosIdentificaciones();
		this.numero_digito = 0;
		this.template = _.template($("#documento_identificacion_template").html());
		this.render();
	}

	events()
	{
		return {
				  "change #id_documento_identificacion"  			  : "select_documento_identificacion",
			   };
	}

	select_documento_identificacion(e)
	{
		if($("#id_documento_identificacion").val() == "")
		{
			this.numero_digito = 0;
		}
		else
		{
			this.numero_digito = this.documentos_identificaciones.get($("#id_documento_identificacion").val()).get("numero_digito");
		}

		$("#id_numero_documento_identificacion").attr({
			"maxlength": this.numero_digito,
			"minlength": this.numero_digito,
		});
	}
  render()
	{
    this.$el.html(this.template());
		return this;
  }

}

module.exports = SelectInputDocumentoIdentificacionUpdate;
