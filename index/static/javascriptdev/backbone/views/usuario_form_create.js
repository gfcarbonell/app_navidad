var $           = require("jquery");
var _           = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $;
var Usuario = require("../models/usuario");




class UsuarioFormCreateView extends Backbone.View
{
	initialize()
	{
		this.template = _.template($("#usuario_form_create_template").html());
		this.render();
        
        _.bindAll(this, 'submit_add');
	}
	events()
	{
		return { 
				"submit"  			  : "submit_add",
				"keyup #id_password1" : "coincidir_password",
				"keyup #id_password2" : "coincidir_password", 
			   };
	}

    render() 
	{
        this.$el.html(this.template());
		return this;
    }

    coincidir_password(e)
    {
    	e.preventDefault();
    	var password1 = $("#id_password1").val();
    	var password2 = $("#id_password2").val();
    	if(password1.length === password2.length)
    	{
    		console.log("1");
    	}
    	else if (password2.length === password1.length)
    	{
    		console.log("2");
    	}
    	else
    	{
    		console.log("3");
    	}
    }
    submit_add(e)
    {
    	
    }	

}

module.exports = UsuarioFormCreateView;
