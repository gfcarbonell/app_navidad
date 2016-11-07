var Backbone = require("backbone");
var $ 		 = require("jquery");
var _        = require("underscore");
Backbone.$ = $;


class SliderView extends Backbone.View 
{
	tagName() { return "figure"; }

    initialize() 
    {
    	this.template = _.template($("#item_slider_template").html());
    	this.listenTo(this.model, "change", this.render, this);
 	}
	render()
	{
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
}

module.exports = SliderView;