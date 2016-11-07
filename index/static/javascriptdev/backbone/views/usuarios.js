var $ 		 	  			  = require("jquery");
var _        				  = require("underscore");
var Backbone 	  			  = require("backbone");
Backbone.$ = $;
var UsuarioView		  		  = require("../views/usuario");



class UsuariosView extends Backbone.View 
{

	className() { return "table-body"; }

	initialize()
	{
		this.listenTo(this.collection, "sync", this.render);
		this.render();
	}

	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista
		this.collection.each(function(model){
			var usuario_view = new UsuarioView({model: model});
			cache.appendChild(usuario_view.render().el);
		});

		this.$el.append(cache);
	}
}

module.exports = UsuariosView;