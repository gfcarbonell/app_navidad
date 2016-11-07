var $ 		 = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $;


class UsuarioView extends Backbone.View 
{
	tagName() { return "tr"; }
	className() { return "table-body-row-data"; }

    initialize() 
    {
    	this.template = _.template($("#usuario_template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
 	
	render()
	{
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
}

module.exports = UsuarioView;