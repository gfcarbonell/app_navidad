var Backbone 	  			  = require("backbone");
var $ 		 	  			  = require("jquery");
var _        				  = require("underscore");
Backbone.$ = $;
var SliderView		  		  = require("../views/slider");



class SlidersView extends Backbone.View 
{
	tagName() { return "ul"; }

	className() { return "slider"; }

	initialize(){
		this.listenTo(this.collection, "sync", this.render);
		this.render();
	}

	render()
	{
		//Crear Cache 
		var cache = document.createDocumentFragment();
		//Iterar objetos y pasando a la vista
		this.collection.each(function(model){
			var sliderView = new SliderView({model: model});
			cache.appendChild(sliderView.render().el);
		});

		this.$el.append(cache);
	}
}

module.exports = SlidersView;