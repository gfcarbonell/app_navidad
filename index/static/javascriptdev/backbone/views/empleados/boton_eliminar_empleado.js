var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class BotonEliminarEmpleado extends Backbone.View
{
	initialize()
	{
		this.template = _.template($("#").html());
		this.render();
	}
	events()
	{
		return {
				"click #"  			  : "",
			   };
	}

  render()
	{
    this.$el.html(this.template());
		return this;
  }
}

module.exports = BotonEliminarEmpleado;
