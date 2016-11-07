var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class InputNumeroDocumentoIdentificacion extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#numero_documento_identificacion_template").html());
		this.render();
	}

	events()
	{
		return { 
				"keypress #id_model_form_empleado-numero_documento_identificacion" : "input_documento_identificacion",
				"keyup #id_model_form_empleado-numero_documento_identificacion" : "verificar_numero_documento_identificacion",
			   };
	}

	input_documento_identificacion(e)
	{
		var keynum = window.event ? window.event.keyCode : e.which;
        if ((keynum == 8) || (keynum == 46))
        	return true;
		        
		return /\d/.test(String.fromCharCode(keynum));
	}
	verificar_numero_documento_identificacion(e)
	{
		e.preventDefault();
		$.ajax({
					url : "/control-de-asistencia/empleados/",	
					
					type: "GET",

					dataType: "text",
					
					data: {"numero_documento_identificacion":$("#id_model_form_empleado-numero_documento_identificacion").val(),},

					async: true,

					success: function(data){
						
					},	

					error: function (data, textStatus, jqXHR) {
		                var errors = $.parseJSON(data.responseText);
		                console.log(xhr.status + ": " + xhr.responseText);
		                alert(data.responseText);
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

module.exports = InputNumeroDocumentoIdentificacion;
