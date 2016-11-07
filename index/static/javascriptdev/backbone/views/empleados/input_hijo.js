var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class InputHijo extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#input_hijo_template").html());
		this.render();
	}
	events()
	{
		return { 
				"change #id_model_form_empleado-hijo_0"  			  : "disable_input_numero_hijo",
				"change #id_model_form_empleado-hijo_1"  			  : "enable_input_numero_hijo",
			   };
	}
	disable_input_numero_hijo(e)
	{
		var valor = $("#id_model_form_empleado-numero_hijo").val();
				
		if(valor>0)
		{
			$("#id_model_form_empleado-numero_hijo").prop("disabled", true);
			$("#id_model_form_empleado-numero_hijo").val(0);
		}
	}
	enable_input_numero_hijo(e)
	{	var valor = $("#id_model_form_empleado-numero_hijo").val();
		
		if(valor==0)
		{
			$("#id_model_form_empleado-numero_hijo").prop("disabled", false);
			$("#id_model_form_empleado-numero_hijo").val(1);
		}
	}
    render() 
	{
        this.$el.html(this.template());
		return this;
    }

}

module.exports = InputHijo;
